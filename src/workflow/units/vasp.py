from src.workflow.units import BaseUnit


class VaspUnit(BaseUnit):
    """
    Vasp unit parser class.
    """

    def __init__(self, config, *args, **kwargs):
        super(VaspUnit, self).__init__(config, *args, **kwargs)
