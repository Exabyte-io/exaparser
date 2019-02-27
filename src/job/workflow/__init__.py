from src.job.workflow.factory import get_unit


class Workflow(object):
    """
    Workflow parser class.
    """

    def __init__(self, config, work_dir):
        self.config = config
        self.work_dir = work_dir
        self.units = self.config.get("units", [])
        self.subworkflows = self.config.get("subworkflows", [])

    @property
    def materials(self):
        return []

    @property
    def properties(self):
        return []

    def to_json(self):
        return self.config

    def parse(self):
        unit_config = next((unit for unit in self.units if unit.get('head')))
        while True:
            if not unit_config: break
            work_dir = unit_config.get("work_dir", self.work_dir)
            if unit_config["type"] == "subworkflow":
                subworkflow_config = next((s for s in self.subworkflows if s.get('_id') == unit_config.get('_id')))
                Workflow(subworkflow_config, work_dir).parse()
            else:
                unit_config.update(get_unit(unit_config["application"]["name"])(unit_config).to_json())
            unit_config = next((u for u in self.units if u["flowchartId"] == unit_config["flowchart_id"]), None)
