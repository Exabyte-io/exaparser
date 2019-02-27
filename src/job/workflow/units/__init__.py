from express import ExPrESS


class BaseUnit(object):
    """
    Base unit parser class.
    """

    def __init__(self, config, *args, **kwargs):
        self.config = config
        self.args = args
        self.kwargs = kwargs

    @property
    def work_dir(self):
        return self.config["work_dir"]

    @property
    def stdout_file(self):
        return self.config["stdout_file"]

    @property
    def parser_name(self):
        return ""

    @property
    def express(self):
        kwargs = {
            "work_dir": self.work_dir,
            "stdout_file": self.stdout_file
        }
        return ExPrESS(self.parser_name, **kwargs)

    def safely_extract_property(self, property_, *args, **kwargs):
        try:
            return self.express.property(property_, *args, **kwargs)
        except:
            print("unable to extract {}".format(property_))

    @property
    def initial_structures(self):
        return [self.safely_extract_property("material", is_initial_structure=True)]

    @property
    def final_structures(self):
        return [self.safely_extract_property("material", is_final_structure=True)]

    @property
    def results(self):
        return []

    @property
    def monitors(self):
        return [
            {
                "name": "standard_output"
            }
        ]

    @property
    def inputs(self):
        return []
