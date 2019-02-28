class BaseComputeParser(object):
    """
    Base compute parser class.

    Args:
        work_dir (str): full path to working directory.
    """

    def __init__(self, work_dir):
        self.work_dir = work_dir

    @property
    def ppn(self):
        return 1

    @property
    def nodes(self):
        return 1

    @property
    def queue(self):
        return "D"

    @property
    def walltime(self):
        return "01:00:00"

    @property
    def notify(self):
        return "n"

    def to_json(self):
        return {
            "ppn": self.ppn,
            "nodes": self.nodes,
            "queue": self.queue,
            "timeLimit": self.walltime,
            "notify": self.notify
        }
