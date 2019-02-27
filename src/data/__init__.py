class DataHandler(object):
    """
    Base data handler class.

    Args:
        job (src.job.Job)
    """

    def __init__(self, job):
        self.job = job

    def handle(self):
        self.handle_materials()
        self.handle_job()
        self.handle_properties()
        self.handle_files()

    def handle_job(self):
        raise NotImplemented

    def handle_files(self):
        raise NotImplemented

    def handle_materials(self):
        raise NotImplemented

    def handle_properties(self):
        raise NotImplemented
