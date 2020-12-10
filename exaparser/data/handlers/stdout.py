import json
from functools import singledispatchmethod

from .. import DataHandler
from ...job import Job


class StdoutDataHandler(DataHandler):
    """
    Stdout data handler class.

    Args:
        job (exaparser.job.Job)
    """

    def __init__(self, job):
        super(StdoutDataHandler, self).__init__(job)

    def print_json(self, content):
        print(json.dumps(content, indent=4))

    @singledispatchmethod
    def _handle(self, arg):
        raise NotImplementedError(f"Unable to handle argument type '{type(arg)}'.")

    @_handle.register
    def _handle_job(self, job: Job):
        self.print_json(self.job.to_json())

    @_handle.register
    def _handle_list(self, list_: list):
        self.print_json(list_)

    def handle(self):
        """
        Prints the job in standard output.
        """
        self._handle(self.job)
