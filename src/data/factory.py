from src.data.handlers.disk import DiskDataHandler
from src.data.handlers.stdout import StdoutDataHandler
from src.data.handlers.exabyte import ExabyteRESTFulAPIDataHandler


def get_data_handler(handler="stdout", *args, **kwargs):
    handlers = dict(stdout=StdoutDataHandler, disk=DiskDataHandler, exabyte=ExabyteRESTFulAPIDataHandler)
    return handlers[handler](*args, **kwargs)
