import os

from exaparser.utils import read
from .. import BaseUnit


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

    @property
    def stdout_file(self):
        return os.path.join(self.work_dir, self.config.get("stdoutFile", '.'.join((self.name, 'out'))))

    @property
    def application(self):
        """
        Returns the application used in the unit.
        Override upon inheritance.

        Returns:
             dict
        """
        raise NotImplementedError

    @property
    def version(self):
        """
        Returns the application version used in the unit.

        Returns:
             str
        """
        raise NotImplementedError

    @property
    def executable(self):
        """
        Returns the executable used in the unit.
        Override upon inheritance.

        Returns:
             dict
        """
        raise NotImplementedError

    @property
    def input(self):
        """
        Returns a list of input files used in the unit.

        Note: Make sure to set "isManuallyChanged" to True.

        Returns:
             list[dict]
        """
        input_ = []
        for config in self.config.get("input", []):
            path_ = os.path.join(self.work_dir, config["name"])
            input_.append({
                "name": config["name"],
                "isManuallyChanged": True,
                "rendered": read(path_) if os.path.exists(path_) else ""
            })
        return input_

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
                "trackedAt": int(os.path.getmtime(self.work_dir)),
                "status": self.status
            }
        ]

    @property
    def results(self):
        """
        Returns a list of property names extracted from the unit.

        Returns:
             list[dict]
        """
        return self.config.get("results", [])

    @property
    def monitors(self):
        """
        Returns a list of monitors used in the unit.

        Returns:
             list[dict]
        """
        return self.config.get("monitors", [])
