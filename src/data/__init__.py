class DataHandler(object):
    """
    Base data handler class.

    Args:
        job (src.job.Job)
    """

    def __init__(self, job):
        self.job = job

    def handle(self):
        raise NotImplemented
