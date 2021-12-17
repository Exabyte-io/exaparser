class DataHandler(object):
    """
    Base data handler class.

    Args:
        job (exaparser.job.Job): an instance of the job class.
    """

    def __init__(self, job):
        self.job = job

    def handle(self):
        """
        Implement the logic to handle extracted job, materials and properties.
        Override upon inheritance.
        """
        raise NotImplementedError
