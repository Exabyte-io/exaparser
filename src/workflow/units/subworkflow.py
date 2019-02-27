from src.workflow.units import BaseUnit


class SubworkflowUnit(BaseUnit):
    """
    Base subworkflow unit parser class.
    """

    def __init__(self, config, work_dir):
        super(SubworkflowUnit, self).__init__(config, work_dir)
        self.id = self.config["id"]

    def to_json(self):
        config = super(SubworkflowUnit, self).to_json()
        config.update({
            "_id": self.id
        })
        return config
