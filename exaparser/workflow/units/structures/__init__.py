class StructuresUnit(object):
    """
    Structures parser class.

    Args:
        config (dict): structures config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        self.config = config
        self.work_dir = work_dir

    def structures(self):
        raise NotImplementedError()

    def to_json(self):
        """
        Returns the structures in JSON format.

        Returns:
             dict
        """
        return {
            "structures": self.structures(),
            "isMultiMaterial": True  # to let job have multiple materials
        }
