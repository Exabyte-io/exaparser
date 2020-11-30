import json

from .. import DataHandler


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

    def handle(self):
        """
        Prints the job in standard output.
        """
        self.print_json(self.job.to_json())
