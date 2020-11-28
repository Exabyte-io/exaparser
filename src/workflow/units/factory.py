from src.workflow.units.subworkflow import SubworkflowUnit
from src.workflow.units.execution.modeling.vasp import VaspExecutionUnit
from src.workflow.units.execution.scripting.shell import ShellExecutionUnit
from src.workflow.units.execution.modeling.espresso import EspressoExecutionUnit
from src.workflow.units.execution.scripting.shell_with_results import ShellWithResultsExecutionUnit


def get_unit(config, work_dir):
    """
    Returns a unit by given config.

    Args:
        config (dict): unit configuration obtained from the template.
        work_dir (str): full path to the job working directory.
    """
    if config["type"] == "execution":
        execution_units = dict(shell=ShellExecutionUnit, vasp=VaspExecutionUnit, espresso=EspressoExecutionUnit)
        # Use ShellWithResultsExecutionUnit if parser is asked to extract any results
        if config["application"]["name"] == "shell" and len(config.get("results", [])):
            return ShellWithResultsExecutionUnit(config, work_dir)
        return execution_units[config["application"]["name"]](config, work_dir)

    if config["type"] == "subworkflow":
        return SubworkflowUnit(config, work_dir)
