from src.job.workflow.units import BaseUnit


class EspressoUnit(BaseUnit):
    """
    Espresso unit parser class.
    """

    def __init__(self, config, *args, **kwargs):
        super(EspressoUnit, self).__init__(config, *args, **kwargs)
