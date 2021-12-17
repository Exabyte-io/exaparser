from express import ExPrESS

from .. import BaseExecutionUnit


class ModelingExecutionUnit(BaseExecutionUnit):
    def __init__(self, config, work_dir):
        super(ModelingExecutionUnit, self).__init__(config, work_dir)

    @property
    def parser_name(self):
        """
        Returns the name of the parser to pass to ExPrESS.

        Returns:
             str
        """
        raise NotImplementedError

    def safely_extract_property(self, property_, *args, **kwargs):
        """
        Safely extracts property.

        Args:
            property_ (str): property name.
            args (list): args passed to property extractor.
            kwargs (dict): kwargs passed to property extractor.

        Returns:
             dict
        """
        try:
            express = ExPrESS(self.parser_name, **dict(work_dir=self.work_dir, stdout_file=self.stdout_file))
            return express.property(property_, *args, **kwargs)
        except:
            pass

    @property
    def initial_structures(self):
        """
        Safely returns a list of initial structures used in this unit.

        Returns:
             list
        """
        structures = []
        try:
            express = ExPrESS(self.parser_name, **dict(work_dir=self.work_dir, stdout_file=self.stdout_file))
            for structure_string in express.parser.initial_structure_strings():
                initial_structure = express.property("material", structure_string=structure_string)
                initial_structure["name"] = "initial_structure"
                structures.append(initial_structure)
        except:
            pass
        return structures

    @property
    def final_structures(self):
        """
        Safely returns a list of final structures generated in this unit.

        Returns:
             list
        """
        structures = []
        try:
            express = ExPrESS(self.parser_name, **dict(work_dir=self.work_dir, stdout_file=self.stdout_file))
            for structure_string in express.parser.final_structure_strings():
                final_structure = express.property("material", structure_string=structure_string)
                final_structure["name"] = "final_structure"
                final_structure["repetition"] = 0
                structures.append(final_structure)
        except:
            pass
        return structures

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

        Returns:
             list[dict]
        """
        properties = []
        for name in [r["name"] for r in self.results]:
            if name == "final_structure":
                continue
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
                    }
                })
        return properties
