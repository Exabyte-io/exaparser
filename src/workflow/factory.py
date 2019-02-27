from src.workflow.units.vasp import VaspExecutionUnit
from src.workflow.units.shell import ShellExecutionUnit
from src.workflow.units.subworkflow import SubworkflowUnit
from src.workflow.units.espresso import EspressoExecutionUnit


def get_unit(config, work_dir):
    if config["type"] == "execution":
        execution_units = dict(shell=ShellExecutionUnit, vasp=VaspExecutionUnit, espresso=EspressoExecutionUnit)
        return execution_units[config["application"]["name"]](config, work_dir)

    if config["type"] == "subworkflow":
        return SubworkflowUnit(config, work_dir)
