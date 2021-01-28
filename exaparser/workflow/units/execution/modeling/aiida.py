from express import ExPrESS

from . import ModelingExecutionUnit


class AiidaExecutionUnit(ModelingExecutionUnit):
    """
    Structures from AiiDA archive parser class.

    Args:
        config (dict): structures config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        self.config = config
        self.work_dir = work_dir

    def structures(self):
        express = ExPrESS('aiida-archive', workDir=self.work_dir)
        return express.parser.structures()

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

    type = 'execution'
    status = ''
    application = 'aiida'
