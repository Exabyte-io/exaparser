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
        for subworkflow in self.workflow.subworkflows:
            for unit in subworkflow.units:
                if hasattr(unit, "initial_structures"):
                    for material in unit.initial_structures:
                        materials.append(material)
        return materials

    @property
    def status(self):
        return "finished"

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
            "creator": {
                "slug": settings.CREATOR
            },
            "owner": {
                "slug": settings.OWNER
            },
            "name": self.name,
            "status": self.status,
            "workDir": self.work_dir,
            "workflow": self.workflow.to_json()
        }
