import os

from exaparser.config import ExaParserConfig
from exaparser.utils import write_json
from .. import DataHandler


class DiskDataHandler(DataHandler):
    """
    Disk data handler class.

    Args:
        job (exaparser.job.Job)
    """

    def __init__(self, job):
        super(DiskDataHandler, self).__init__(job)

    def handle(self):
        """
        Stores job inside data_dir directory.
        """
        data_dir = os.path.join(self.job.work_dir, ExaParserConfig.get("disk_data_handler", "data_dir"))
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        write_json(os.path.join(data_dir, "job.json"), self.job.to_json())
