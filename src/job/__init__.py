import os

from src.config import ExaParserConfig
from src.utils import read_json, find_file
from src.workflow.workflow import Workflow
from src.job.compute.factory import get_compute_parser


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
    def materials(self):
        """
        Returns a list of materials (initial_structures) used in job.

        Returns:
             list[dict]
        """
        materials = []
        for unit in self.workflow.execution_units:
            materials.extend(unit.initial_structures)
        return materials

    @property
    def stdout_files(self):
        """
        Returns a list of stdout files for all execution units.

        Returns:
             list[dict]
        """
        stdout_files = []
        for unit in self.workflow.execution_units:
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
            properties.extend(unit.properties)
        return properties

    @property
    def workflow(self):
        """
        Returns an instance of Workflow class.
        """
        if not self._workflow:
            self._workflow = Workflow(self.get_workflow_template(), self.work_dir)
        return self._workflow

    def get_workflow_template(self):
        templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
        if self.is_espresso_job:
            template_path = os.path.join(templates_dir, "espresso.json")
        elif self.is_vasp_job:
            template_path = os.path.join(templates_dir, "vasp.json")
        else:
            template_path = os.path.join(templates_dir, "shell.json")
        return read_json(template_path)

    @property
    def is_vasp_job(self):
        return find_file(ExaParserConfig["global"]["vasp_xml_file"], self.work_dir) is not None

    @property
    def is_espresso_job(self):
        return find_file(ExaParserConfig["global"]["espresso_xml_file"], self.work_dir) is not None

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
