import os

from src import settings
from src.data import DataHandler
from src.utils import write_json


class DiskDataHandler(DataHandler):
    """
    Disk data handler class.

    Args:
        job (src.job.Job)
    """

    def __init__(self, job):
        super(DiskDataHandler, self).__init__(job)

    def handle(self):
        """
        Stores job inside settings.DISK_DATA_HANDLER_DATA_DIR_NAME directory.
        """
        data_dir = os.path.join(self.job.work_dir, settings.DISK_DATA_HANDLER_DATA_DIR_NAME)
        if not os.path.exists(data_dir): os.makedirs(data_dir)
        write_json(os.path.join(data_dir, "job.json"), self.job.to_json())
