from .execution.modeling.espresso import EspressoExecutionUnit
from .execution.modeling.vasp import VaspExecutionUnit
from .execution.scripting.shell import ShellExecutionUnit
from .execution.scripting.shell_with_results import ShellWithResultsExecutionUnit
from .subworkflow import SubworkflowUnit


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
