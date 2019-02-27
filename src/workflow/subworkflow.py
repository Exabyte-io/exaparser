from src.workflow.units.factory import get_unit


class Subworkflow(object):
    """
    Subworkflow parser class.

    Args:
        config (dict): subworkflow config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        self.config = config
        self.work_dir = work_dir
        self.units = [get_unit(config, self.work_dir) for config in self.config.get("units", [])]

    @property
    def id(self):
        return self.config["_id"]

    @property
    def name(self):
        return self.config.get("name", "Subworkflow")

    @property
    def application(self):
        return self.config["application"]

    @property
    def model(self):
        return self.config["model"]

    @property
    def properties(self):
        return []

    def to_json(self):
        return {
            "_id": self.id,
            "name": self.name,
            "model": self.model,
            "properties": self.properties,
            "application": self.application,
            "units": [u.to_json() for u in self.units]
        }
