from src.job.workflow.units.vasp import VaspUnit
from src.job.workflow.units.shell import ShellUnit
from src.job.workflow.units.espresso import EspressoUnit


def get_unit(name="shell", *args, **kwargs):
    units = dict(shell=ShellUnit, vasp=VaspUnit, espresso=EspressoUnit)
    return units[name](*args, **kwargs)
