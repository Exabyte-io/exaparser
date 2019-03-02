from src.workflow.units.subworkflow import SubworkflowUnit
from src.workflow.units.execution.vasp import VaspExecutionUnit
from src.workflow.units.execution.shell import ShellExecutionUnit
from src.workflow.units.execution.espresso import EspressoExecutionUnit


def get_unit(config, work_dir):
    if config["type"] == "execution":
        execution_units = dict(shell=ShellExecutionUnit, vasp=VaspExecutionUnit, espresso=EspressoExecutionUnit)
        return execution_units[config["application"]["name"]](config, work_dir)

    if config["type"] == "subworkflow":
        return SubworkflowUnit(config, work_dir)
