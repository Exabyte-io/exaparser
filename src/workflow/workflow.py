from src.workflow.units.factory import get_unit
from src.workflow.subworkflow import Subworkflow


class Workflow(object):
    """
    Workflow parser class.

    Args:
        config (dict): workflow config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        self.config = config
        self.work_dir = work_dir
        self.units = [get_unit(config, self.work_dir) for config in self.config.get("units", [])]
        self.subworkflows = [Subworkflow(config, self.work_dir) for config in self.config.get("subworkflows", [])]

    @property
    def name(self):
        return self.config.get("name", "Workflow")

    @property
    def properties(self):
        return []

    @property
    def execution_units(self):
        execution_units = []
        for subworkflow in self.subworkflows:
            execution_units.extend(subworkflow.execution_units)
        return execution_units

    def to_json(self):
        return {
            "name": self.name,
            "properties": self.properties,
            "units": [u.to_json() for u in self.units],
            "subworkflows": [u.to_json() for u in self.subworkflows],
        }
