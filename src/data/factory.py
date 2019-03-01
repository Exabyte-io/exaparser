from src.data.handlers.disk import DiskDataHandler
from src.data.handlers.stdout import StdoutDataHandler
from src.data.handlers.exabyte import ExabyteRESTFulAPIDataHandler


def get_data_handler(name, job):
    handlers = dict(STDOUT=StdoutDataHandler, DISK=DiskDataHandler, ExabyteRESTFulAPI=ExabyteRESTFulAPIDataHandler)
    return handlers[name](job)
