import os
import time

from express import ExPrESS

from src import settings
from src.utils import find_file
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
        self.work_dir = os.path.join(self.work_dir, self.config.get("workDir", ""))
        self.stdout_file = os.path.join(self.work_dir, self.config.get("stdoutFile", '.'.join((self.name, 'out'))))
        self.express = ExPrESS(self.parser_name, **dict(work_dir=self.work_dir, stdout_file=self.stdout_file))

    @property
    def parser_name(self):
        """
        Returns the name of the parser to pass to ExPrESS.

        Returns:
             str: espresso or vasp
        """
        if find_file(settings.VASP_XML_FILE, self.work_dir): return "vasp"
        if find_file(settings.ESPRESSO_XML_FILE, self.work_dir): return "espresso"

    @property
    def application(self):
        """
        Returns the application used in the unit.
        Override upon inheritance.

        Returns:
             dict
        """
        raise NotImplemented

    @property
    def executable(self):
        """
        Returns the executable used in the unit.
        Override upon inheritance.

        Returns:
             dict
        """
        raise NotImplemented

    @property
    def input(self):
        """
        Returns a list of input files used in the unit.
        Override upon inheritance.

        Note: Make sure to set "isManuallyChanged" to True.

        Returns:
             list[dict]
        """
        raise NotImplemented

    @property
    def postProcessors(self):
        """
        Returns a list of postProcessors used in the unit.
        Override upon inheritance as necessary.

        Returns:
             list[dict]
        """
        return self.config.get("postProcessors", [])

    @property
    def preProcessors(self):
        """
        Returns a list of preProcessors used in the unit.
        Override upon inheritance as necessary.

        Returns:
             list[dict]
        """
        return self.config.get("preProcessors", [])

    def to_json(self):
        """
        Returns the unit in JSON format.

        Returns:
             dict
        """
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
        """
        Returns unit status.

        Note: This is a placeholder for future to extract unit status based on unit outputs.

        Returns:
             str
        """
        return "finished"

    @property
    def status_track(self):
        """
        Returns unit status track.

        Returns:
             list[dict]
        """
        return [
            {
                "trackedAt": time.time(),
                "status": self.status
            }
        ]

    def safely_extract_property(self, property_, safe=True, *args, **kwargs):
        """
        Safely extracts property.

        Args:
            property_ (str): property name.
            safe (bool): whether to raise exception if property cannot be extracted.
            args (list): args passed to property extractor.
            kwargs (dict): kwargs passed to property extractor.

        Returns:
             dict
        """
        try:
            return self.express.property(property_, *args, **kwargs)
        except:
            if not safe:
                raise

    @property
    def initial_structures(self):
        """
        Returns a list of initial structures used in this unit.

        Returns:
             list
        """
        initial_structure = self.safely_extract_property("material", False, is_initial_structure=True)
        initial_structure["name"] = "initial_structure"
        return [initial_structure]

    @property
    def final_structures(self):
        """
        Returns a list of final structures generated in this unit.

        Returns:
             list
        """
        final_structure = self.safely_extract_property("material", False, is_final_structure=True)
        final_structure["name"] = "final_structure"
        final_structure["repetition"] = 0
        return [final_structure]

    @property
    def results(self):
        """
        Returns a list of property names extracted from the unit.

        Returns:
             list[dict]
        """
        return [{"name": name} for name in settings.PROPERTIES]

    @property
    def structures(self):
        """
        Returns a list of structure pairs (initial/final) extracted from the unit.

        Returns:
             list[dict]
        """
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
        """
        Returns a list of properties in EDC format extracted from the unit.

        Note: structures are added to each property to properly associate properties with initial/final structure.

        Returns:
             list[dict]
        """
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
        """
        Returns a list of monitors used in the unit.

        Returns:
             list[dict]
        """
        return [
            {
                "name": "standard_output"
            }
        ]
