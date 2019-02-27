from src.data import DataHandler


class DiskDataHandler(DataHandler):
    """
    Disk data handler class.
    """

    def __init__(self, job):
        super(DiskDataHandler, self).__init__(job)
