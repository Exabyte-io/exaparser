import os
import time

from express import ExPrESS
from slugify import slugify

from src import settings
from src.workflow.units import BaseUnit


class BaseExecutionUnit(BaseUnit):
    """
    Base execution unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        super(BaseExecutionUnit, self).__init__(config, work_dir)
        self.work_dir = self.config.get("work_dir", self.work_dir)
        self.express = ExPrESS(self.express_parser_name, **dict(work_dir=self.work_dir, stdout_file=self.stdout_file))

    @property
    def stdout_file(self):
        return os.path.join(self.work_dir, self.config.get("stdout_file", '.'.join((slugify(self.name), 'out'))))

    @property
    def express_parser_name(self):
        return self.application["name"]

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
            "type": "execution",
            "status": self.status,
            "statusTrack": self.status_track,
        })
        return config

    @property
    def status(self):
        return "finished"

    @property
    def status_track(self):
        return [
            {
                "trackedAt": time.time(),
                "status": self.status
            }
        ]

    def safely_extract_property(self, property_, safe=True, *args, **kwargs):
        try:
            return self.express.property(property_, *args, **kwargs)
        except:
            if not safe:
                raise

    @property
    def initial_structures(self):
        initial_structure = self.safely_extract_property("material", False, is_initial_structure=True)
        initial_structure["name"] = "initial_structure"
        return [initial_structure]

    @property
    def final_structures(self):
        final_structure = self.safely_extract_property("material", False, is_final_structure=True)
        final_structure["name"] = "final_structure"
        final_structure["repetition"] = 0
        return [final_structure]

    @property
    def results(self):
        return [{"name": name} for name in settings.PROPERTIES]

    @property
    def structures(self):
        structures = []
        final_structures = self.final_structures
        initial_structures = self.initial_structures
        for index, structure in enumerate(initial_structures):
            structures.append({
                "initial": structure,
                "final": final_structures[index]
            })
            return structures

    @property
    def properties(self):
        properties = []
        structures = self.structures
        for name in settings.PROPERTIES:
            property_ = self.safely_extract_property(name)
            if property_:
                property_.update({"repetition": 0})
                properties.append({
                    "data": property_,
                    "source": {
                        "type": "exabyte",
                        "info": {
                            "unitId": self.flowchartId
                        }
                    },
                    "structures": structures,
                })
        return properties

    @property
    def monitors(self):
        return [
            {
                "name": "standard_output"
            }
        ]
