import os

from express import ExPrESS

from src import settings
from src.workflow.units import BaseUnit


class BaseExecutionUnit(BaseUnit):
    """
    Base execution unit parser class.
    """

    def __init__(self, config, work_dir):
        super(BaseExecutionUnit, self).__init__(config, work_dir)
        self.work_dir = self.config.get("work_dir", self.work_dir)
        self.stdout_file = os.path.join(self.work_dir, self.config.get("stdout_file", ""))
        self.express = ExPrESS(self.express_parser_name, work_dir=self.work_dir, stdout_file=self.stdout_file)

    @property
    def express_parser_name(self):
        return self.application["name"]

    @property
    def name(self):
        return self.config.get("name", "Unit")

    @property
    def application(self):
        raise NotImplemented

    @property
    def executable(self):
        raise NotImplemented

    @property
    def input(self):
        raise NotImplemented

    @property
    def postProcessors(self):
        return self.config.get("postProcessors", [])

    @property
    def preProcessors(self):
        return self.config.get("preProcessors", [])

    def to_json(self):
        config = super(BaseExecutionUnit, self).to_json()
        config.update({
            "application": self.application,
            "executable": self.executable,
            "input": self.input,
            "monitors": self.monitors,
            "name": self.name,
            "postProcessors": self.postProcessors,
            "preProcessors": self.preProcessors,
            "results": self.results,
            "type": "execution"
        })
        return config

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
        properties = []
        for name in settings.PROPERTIES:
            property_ = self.safely_extract_property(name)
            if property_: properties.append(property_)
        return properties

    @property
    def monitors(self):
        return [
            {
                "name": "standard_output"
            }
        ]
