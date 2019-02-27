class BaseComputeParser(object):
    """
    Base compute parser class.
    """

    def __init__(self, work_dir):
        self.work_dir = work_dir

    @property
    def ppn(self):
        return 1

    @property
    def nodes(self):
        return 1

    @property
    def queue(self):
        return "D"

    @property
    def walltime(self):
        return "01:00:00"

    @property
    def notify(self):
        return "n"

    @property
    def job_id(self):
        return ""

    @property
    def cluster_fqdn(self):
        return "external"

    def to_json(self):
        return {
            "ppn": self.ppn,
            "nodes": self.nodes,
            "queue": self.queue,
            "timeLimit": self.walltime,
            "notify": self.notify,
            "cluster": {
                "jid": self.job_id,
                "fqdn": self.cluster_fqdn
            }
        }
