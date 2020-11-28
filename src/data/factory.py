from src.data.handlers.disk import DiskDataHandler
from src.data.handlers.exabyte import ExabyteRESTFulAPIDataHandler
from src.data.handlers.stdout import StdoutDataHandler


def get_data_handler(name, job):
    """
    Returns an instance of the data handler class.

    Args:
        name (str): data handler name, STDOUT, DISK or ExabyteRESTFulAPI
        job (src.job.Job): an instance of the job class.
    """
    handlers = dict(STDOUT=StdoutDataHandler, DISK=DiskDataHandler, ExabyteRESTFulAPI=ExabyteRESTFulAPIDataHandler)
    return handlers[name](job)
