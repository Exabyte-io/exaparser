class BaseUnit(object):
    """
    Base unit parser class.
    """

    def __init__(self, config, work_dir):
        self.config = config
        self.work_dir = work_dir
        self.type = self.config["type"]
        self.head = self.config.get("head", False)
        self.flowchartId = self.config["flowchartId"]
        self.next_flowchartId = self.config.get("next", "")

    def to_json(self):
        return {
            "flowchartId": self.flowchartId,
            "head": self.head,
            "type": self.type,
            "next": self.next_flowchartId
        }
