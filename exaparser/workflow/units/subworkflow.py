from . import BaseUnit


class SubworkflowUnit(BaseUnit):
    """
    Subworkflow unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        super(SubworkflowUnit, self).__init__(config, work_dir)
        self.id = self.config["_id"]

    def to_json(self):
        """
        Returns the subworkflow unit in JSON format.

        Returns:
             dict
        """
        config = super(SubworkflowUnit, self).to_json()
        config.update({
            "_id": self.id
        })
        return config
