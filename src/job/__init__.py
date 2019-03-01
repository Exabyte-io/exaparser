from src import settings
from src.workflow.workflow import Workflow
from src.job.compute.factory import get_compute_parser


class Job(object):
    """
    Job parser class.

    Args:
        work_dir (str): full path to working directory.
    """

    def __init__(self, work_dir):
        self.work_dir = work_dir
        self._workflow = None
        self._compute = None

    @property
    def compute(self):
        if not self._compute:
            self._compute = get_compute_parser(settings.RMS_TYPE, self.work_dir)
        return self._compute

    @property
    def materials(self):
        materials = []
        for unit in self.workflow.execution_units:
            materials.extend(unit.initial_structures)
        return materials

    @property
    def status(self):
        """
        Returns job status. Status is set to "error" if there is a unit in "error" status.

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
        properties = []
        for unit in self.workflow.execution_units:
            properties.extend(unit.properties)
        return properties

    @property
    def workflow(self):
        if not self._workflow:
            self._workflow = Workflow(settings.WORKFLOW_TEMPLATE, self.work_dir)
        return self._workflow

    @property
    def name(self):
        return settings.JOB_NAME

    def to_json(self):
        return {
            "_project": {
                "slug": settings.PROJECT
            },
            "compute": self.compute.to_json(),
            "owner": {
                "slug": settings.OWNER
            },
            "name": self.name,
            "status": self.status,
            "workDir": self.work_dir,
            "workflow": self.workflow.to_json()
        }
