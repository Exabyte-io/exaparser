import os
import re
import json

from multiprocessing import Pool
from endpoints.jobs import JobEndpoints
from endpoints.projects import ProjectEndpoints
from endpoints.materials import MaterialEndpoints
from endpoints.raw_properties import RawPropertiesEndpoints

from src.data import DataHandler
from src.config import ExaParserConfig
from src.enums import OUTPUT_CHUNK_SIZE
from src.utils import upload_file_to_object_storage


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
        """
        Returns a list of arguments passed to the endpoints.

        Returns:
             list
        """
        return [
            ExaParserConfig.get("exabyte_api_data_handler", "hostname"),
            ExaParserConfig.getint("exabyte_api_data_handler", "port"),
            ExaParserConfig.get("exabyte_api_data_handler", "account_id"),
            ExaParserConfig.get("exabyte_api_data_handler", "auth_token"),
            ExaParserConfig.get("exabyte_api_data_handler", "version"),
            ExaParserConfig.getboolean("exabyte_api_data_handler", "secure")
        ]

    @property
    def owner(self):
        """
        Returns the owner configuration extracted from the project.

        Returns:
             dict
        """
        if not self._owner:
            self._owner = self.project["owner"]
        return self._owner

    @property
    def project(self):
        """
        Returns the project the job should be created in.

        Returns:
             dict
        """
        if not self._project:
            self._project = self.project_endpoints.list(
                {
                    "slug": ExaParserConfig["global"]["project_slug"],
                    "owner.slug": ExaParserConfig["global"]["owner_slug"]
                }
            )[0]
        return self._project

    def create_materials(self):
        """
        Creates materials in web application.

        Returns:
             list
        """
        materials = []
        for config in self.job.materials:
            config["owner"] = self.owner
            materials.append(self.material_endpoints.create(config))
        return materials

    def create_job(self, materials):
        """
        Creates job in web application.

        Note: job must be set as external (isExternal=True) to be able to access the files.

        Returns:
             list
        """
        config = self.job.to_json()
        config["isExternal"] = True
        config["owner"] = self.owner
        config["_project"] = {"_id": self.project["_id"]}
        config["_materials"] = [{"_id": m["_id"]} for m in materials]
        return self.job_endpoints.create(config)

    def create_properties(self, job_id):
        """
        Creates properties in web application. Properties will be shown in job's results tab after creation.

        Args:
            job_id (str): job ID.
        """
        for property_ in self.job.properties:
            property_["source"]["info"]["jobId"] = job_id
            self.raw_properties_endpoints.create(property_)

    @property
    def files(self):
        """
        Returns a list file paths relative to jb working directory to upload to object storage.

        Note: files matching excluded_files_regex are ignored.

        Returns:
             list
        """
        files_ = []
        for root, dirs, files in os.walk(self.job.work_dir):
            for file_ in [os.path.join(root, f) for f in files]:
                regex = ExaParserConfig.get("exabyte_api_data_handler", "excluded_files_regex")
                if regex and re.match(regex, file_): continue
                files_.append(file_.replace("".join((self.job.work_dir, "/")), ""))
        return files_

    def upload_files(self, job_id):
        """
        Uploads the file in parallel into object storage.

        Note: permission to upload files into object storage is given through presignedURLs.

        Args:
            job_id (str): job ID.
        """
        presigned_urls = self.job_endpoints.get_presigned_urls(job_id, self.files)
        presigned_urls = [{"path": os.path.join(self.job.work_dir, p["file"]), "URL": p["URL"]} for p in presigned_urls]
        num_workers = min(len(presigned_urls), ExaParserConfig.getint("exabyte_api_data_handler", "num_workers"))
        pool = Pool(processes=num_workers)
        pool.map(upload_file_to_object_storage, presigned_urls)

    def upload_stdout(self, job_id):
        """
        Uploads stdout file.

        Args:
            job_id (str): job ID.
        """
        headers = self.job_endpoints.headers
        endpoint_path = os.path.join("jobs", job_id, "output-files")
        for config in self.job.stdout_files:
            output_chunks_count = 0
            file_descriptor = open(config["stdoutFile"])
            while True:
                chunk = file_descriptor.read(OUTPUT_CHUNK_SIZE)
                if chunk != '':
                    data = {
                        "chunk": chunk,
                        "repetition": 0,
                        "order": output_chunks_count,
                        "unitFlowchartId": config["unitFlowchartId"],
                    }
                    self.job_endpoints.request('POST', endpoint_path, data=json.dumps(data), headers=headers)
                    output_chunks_count += 1
                else:
                    break

    def handle(self):
        """
        Creates materials, job and properties in webapp and uploads files into object storage.
        """
        materials = self.create_materials()
        job = self.create_job(materials)
        self.create_properties(job["_id"])
        if ExaParserConfig.getboolean("exabyte_api_data_handler", "upload_files"): self.upload_files(job["_id"])
        if ExaParserConfig.getboolean("exabyte_api_data_handler", "upload_stdout_file"): self.upload_stdout(job["_id"])
