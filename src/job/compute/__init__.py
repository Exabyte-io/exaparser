class BaseComputeParser(object):
    """
    Base compute parser class.

    Args:
        work_dir (str): full path to working directory.
    """

    def __init__(self, work_dir):
        self.work_dir = work_dir

    @property
    def ppn(self):
        """
        Returns number of processors per node.
        Override on child classes.

        Returns:
             int
        """
        return 1

    @property
    def nodes(self):
        """
        Returns number of nodes.
        Override on child classes.

        Returns:
             int
        """
        return 1

    @property
    def queue(self):
        """
        Returns queue name.
        Override on child classes.

        Returns:
             int
        """
        return "D"

    @property
    def walltime(self):
        """
        Returns job walltime.
        Override on child classes.

        Returns:
             int
        """
        return "01:00:00"

    def to_json(self):
        return {
            "ppn": self.ppn,
            "nodes": self.nodes,
            "queue": self.queue,
            "timeLimit": self.walltime
        }
