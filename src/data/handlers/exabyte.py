from endpoints.jobs import JobEndpoints
from endpoints.projects import ProjectEndpoints
from endpoints.materials import MaterialEndpoints
from endpoints.raw_properties import RawPropertiesEndpoints

from src import settings
from src.data import DataHandler


class ExabyteRESTFulAPIDataHandler(DataHandler):
    """
    Exabyte RESTFul API data handler class.

    Args:
        job (src.job.Job)
    """

    def __init__(self, job):
        super(ExabyteRESTFulAPIDataHandler, self).__init__(job)
        self._owner = self._project = None
        self.job_endpoints = JobEndpoints(*self.endpoint_args)
        self.project_endpoints = ProjectEndpoints(*self.endpoint_args)
        self.material_endpoints = MaterialEndpoints(*self.endpoint_args)
        self.raw_properties_endpoints = RawPropertiesEndpoints(*self.endpoint_args)

    @property
    def endpoint_args(self):
        return [settings.API_HOSTNAME, settings.API_PORT, settings.API_ACCOUNT_ID,
                settings.API_AUTH_TOKEN, settings.API_VERSION, settings.API_SECURE]

    @property
    def owner(self):
        if not self._owner:
            self._owner = self.project["owner"]
        return self._owner

    @property
    def project(self):
        if not self._project:
            self._project = self.project_endpoints.list({"slug": settings.PROJECT, "owner.slug": settings.OWNER})[0]
        return self._project

    def create_materials(self):
        materials = []
        for config in self.job.materials:
            config["owner"] = self.owner
            materials.append(self.material_endpoints.create(config))
        return materials

    def create_job(self, materials):
        config = self.job.to_json()
        config["owner"] = self.owner
        config["_project"] = {"_id": self.project["_id"]}
        config["_material"] = {"_id": materials[0]["_id"]}
        return self.job_endpoints.create(config)

    def create_properties(self, job):
        for property_ in self.job.properties:
            property_["source"]["info"]["jobId"] = job["_id"]
            self.raw_properties_endpoints.create(property_)

    def handle(self):
        materials = self.create_materials()
        job = self.create_job(materials)
        self.create_properties(job)
