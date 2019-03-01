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
        """
        Returns compute parser class to extract compute configuration.
        """
        if not self._compute:
            self._compute = get_compute_parser(settings.RMS_TYPE, self.work_dir)
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
            self._workflow = Workflow(settings.WORKFLOW_TEMPLATE, self.work_dir)
        return self._workflow

    @property
    def name(self):
        """
        Returns the job name.

        Note: This is a placeholder for future to implement advanced logic for setting job name.

        Returns:
            str
        """
        return settings.JOB_NAME

    def to_json(self):
        """
        Returns the job in JSON format.

        Returns:
             dict
        """
        return {
            "_project": {
                "slug": settings.PROJECT_SLUG
            },
            "compute": self.compute.to_json(),
            "owner": {
                "slug": settings.OWNER_SLUG
            },
            "name": self.name,
            "status": self.status,
            "workDir": self.work_dir,
            "workflow": self.workflow.to_json()
        }
