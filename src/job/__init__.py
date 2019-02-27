from src import settings
from src.workflow import Workflow
from src.job.compute.factory import get_compute_parser


class Job(object):
    """
    Job parser class.
    """

    def __init__(self, work_dir, *args, **kwargs):
        self.work_dir = work_dir

    @property
    def compute(self):
        return get_compute_parser(settings.RMS_TYPE, self.work_dir)

    @property
    def status(self):
        return "finished"

    @property
    def workflow(self):
        return Workflow(self.work_dir)

    @property
    def name(self):
        return "".join((settings.JOB_PREFIX, ""))

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

    def parse(self):
        for handler in settings.DATA_HANDLERS:
            handler.parse(self)
