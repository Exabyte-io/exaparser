from src.data.disk import DiskDataHandler
from src.data.stdout import StdoutDataHandler
from src.data.exabyte import ExabyteRESTFulAPIDataHandler


def get_data_handler(handler="stdout", *args, **kwargs):
    handlers = dict(stdout=StdoutDataHandler, disk=DiskDataHandler, exabyte=ExabyteRESTFulAPIDataHandler)
    return handlers[handler](*args, **kwargs)
