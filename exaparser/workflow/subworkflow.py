from .units.factory import get_unit


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
        """
        Returns subworkflow id.

        Returns:
             str
        """
        return self.config["_id"]

    @property
    def name(self):
        """
        Returns subworkflow name.

        Returns:
             str
        """
        return self.config.get("name", "Subworkflow")

    @property
    def application(self):
        """
        Returns the application used in the subworkflow.

        Note: This is a placeholder for future to extract application from disk.

        Returns:
             dict
        """
        return self.units[0].application

    @property
    def model(self):
        """
        Returns the model used in the subworkflow.

        Note: This is a placeholder for future to extract model from disk.

        Returns:
             dict
        """
        return self.config["model"]

    @property
    def execution_units(self):
        """
        Returns a list of all execution units in this subworkflow.

        Returns:
             list
        """
        execution_units = []
        for unit in self.units:
            if unit.type == "execution":
                execution_units.append(unit)
        return execution_units

    def to_json(self):
        """
        Returns the subworkflow in JSON format.

        Returns:
             dict
        """
        return {
            "_id": self.id,
            "name": self.name,
            "model": self.model,
            "properties": [],
            "application": self.application,
            "units": [u.to_json() for u in self.units]
        }
