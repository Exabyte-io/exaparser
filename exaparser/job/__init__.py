import os

from exaparser.config import ExaParserConfig
from exaparser.utils import read_json
from .compute.factory import get_compute_parser
from ..workflow.workflow import Workflow


class Job(object):
    """
    Job parser class.

    Args:
        work_dir (str): full path to working directory.
    """

    def __init__(self, name, work_dir):
        self.name = name
        self.work_dir = work_dir
        self._workflow = None
        self._compute = None

    @property
    def compute(self):
        """
        Returns compute parser class to extract compute configuration.
        """
        if not self._compute:
            self._compute = get_compute_parser(ExaParserConfig["global"]["rms_type"], self.work_dir)
        return self._compute

    @property
    def structures(self):
        """
        Returns a list of structures (initial/final) used in job.

        Returns:
             list[dict]
        """
        structures = []
        for unit in self.workflow.execution_units:
            structures.extend(getattr(unit, "structures", []))
        return structures

    @property
    def stdout_files(self):
        """
        Returns a list of stdout files for all execution units.

        Returns:
             list[dict]
        """
        stdout_files = []
        for unit in self.workflow.execution_units:
            if os.path.exists(unit.stdout_file):
                stdout_files.append({
                    "stdoutFile": unit.stdout_file,
                    "unitFlowchartId": unit.flowchartId,
                })
        return stdout_files

    @property
    def status(self):
        """
        Returns job status.
        Status is set to "error" if there is a unit in "error" status.

        Returns:
             str
        """
        status = "finished"
        for unit in self.workflow.execution_units:
            if unit.status == "error":
                status = "error"
        return status

    @property
    def properties(self):
        """
        Returns a list of all properties extracted from the job.

        Returns:
             list[dict]
        """
        properties = []
        for unit in self.workflow.execution_units:
            properties.extend(getattr(unit, "properties", []))
        return properties

    @property
    def workflow(self):
        """
        Returns an instance of Workflow class.
        """
        if not self._workflow:
            templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
            template_path = os.path.join(templates_dir, ExaParserConfig["global"]["workflow_template_name"])
            self._workflow = Workflow(read_json(template_path), self.work_dir)
        return self._workflow

    def to_json(self):
        """
        Returns the job in JSON format.

        Returns:
             dict
        """
        return {
            "_project": {
                "slug": ExaParserConfig["global"]["project_slug"]
            },
            "compute": self.compute.to_json(),
            "owner": {
                "slug": ExaParserConfig["global"]["owner_slug"]
            },
            "name": self.name,
            "status": self.status,
            "workDir": self.work_dir,
            "workflow": self.workflow.to_json()
        }
