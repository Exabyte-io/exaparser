import json

from src.data import DataHandler


class StdoutDataHandler(DataHandler):
    """
    Stdout data handler class.

    Args:
        job (src.job.Job)
    """

    def __init__(self, job):
        super(StdoutDataHandler, self).__init__(job)

    def print_json(self, content):
        print(json.dumps(content, indent=4))

    def handle_job(self):
        self.print_json(self.job.to_json())

    def handle_materials(self):
        self.print_json(self.job.materials)

    def handle_files(self):
        pass

    def handle_properties(self):
        pass
