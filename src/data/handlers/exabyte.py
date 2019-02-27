from src.data import DataHandler


class ExabyteRESTFulAPIDataHandler(DataHandler):
    """
    Exabyte RESTFul API data handler class.

    Args:
        job (src.job.Job)
    """

    def __init__(self, job):
        super(ExabyteRESTFulAPIDataHandler, self).__init__(job)

    def handle(self):
        pass
