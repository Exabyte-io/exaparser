class BaseUnit(object):
    """
    Base unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        self.config = config
        self.work_dir = work_dir
        self.type = self.config["type"]
        self.name = self.config.get("name", "")
        self.head = self.config.get("head", False)
        self.flowchartId = self.config["flowchartId"]
        self.next_flowchartId = self.config.get("next", "")

    def to_json(self):
        """
        Returns the unit in JSON format.

        Returns:
             dict
        """
        return {
            "flowchartId": self.flowchartId,
            "name": self.name,
            "head": self.head,
            "type": self.type,
            "next": self.next_flowchartId
        }
