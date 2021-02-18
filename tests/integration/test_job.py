import os

import requests_mock
from exaparser.data.factory import get_data_handler
from exaparser.job import Job
from exaparser.utils import read_json
from tests.enums import FIXTURES_DIR
from tests.integration import IntegrationTestBase


class TestJobParser(IntegrationTestBase):

    def setUp(self):
        super(TestJobParser, self).setUp()

    def tearDown(self):
        super(TestJobParser, self).setUp()

    def _clean_job_config(self, config):
        # These non-deterministic values in the results need to be overwritten with mock values, so
        # that our test comparisons work.
        config["workDir"] = "/mock/path"
        config["workflow"]["subworkflows"][0]["units"][0]["statusTrack"][0]["trackedAt"] = 1234567890

    def test_espresso_001_shell_job(self):
        """
        Extracts a job from an espresso calculation and asserts the results.
        """
        expected = read_json(os.path.join(FIXTURES_DIR, "espresso", "shell-job.json"))

        actual = Job("External Job", os.path.join(FIXTURES_DIR, "espresso", "test-001")).to_json()
        self._clean_job_config(actual)

        self.assertDeepAlmostEqual(expected, actual)

    def test_vasp_001_shell_job(self):
        """
        Extracts a job from a vasp calculation and asserts the results.
        """
        expected = read_json(os.path.join(FIXTURES_DIR, "vasp", "shell-job.json"))

        actual = Job("External Job", os.path.join(FIXTURES_DIR, "vasp", "test-001")).to_json()
        self._clean_job_config(actual)

        self.assertDeepAlmostEqual(expected, actual)

    def test_aiida_001_shell_job(self):
        """
        Extracts a job from a aiida calculation and asserts the results.
        """
        expected = read_json(os.path.join(FIXTURES_DIR, "aiida", "shell-job.json"))

        actual = Job("External Job", os.path.join(FIXTURES_DIR, "aiida", "test-001")).to_json()
        self._clean_job_config(actual)

        self.assertDeepAlmostEqual(expected, actual)

    @requests_mock.Mocker()
    def test_aiida_001_shell_job_upload_to_platform(self, mocker):

        def project_endpoint_json_response(request, context):
            return {'status': 'success', 'data': [{'_id': '', 'owner': 'demo'}]}

        mocker.get(
            'https://platform.exabyte.io:443/api/2018-10-01/projects',
            json=project_endpoint_json_response,
            status_code=200)

        def jobs_create_endpoint_json_response(request, context):
            data = request.json()
            data.setdefault('_id', '')
            return {'status': 'success', 'data': data}

        mocker.put(
            'https://platform.exabyte.io:443/api/2018-10-01/jobs/create',
            json=jobs_create_endpoint_json_response,
            status_code=200)

        def structures_endpoint_json_response(request, context):
            from pprint import pprint;
            request_data = request.json()
            self.assertIn('structures', request_data)
            self.assertEqual(len(request_data['structures']), 39)
            return {'status': 'success', 'data': {}}

        mocker.post(
            'https://platform.exabyte.io:443/api/2018-10-01/structures/',
            json=structures_endpoint_json_response,
            status_code=200)

        url_s3_bucket = 'https://bucket.s3.example.com/abc'
        mocker.put(url_s3_bucket, status_code=200)

        def jobs_presigned_urls_json_response(request, context):
            return {
                'status': 'success',
                'data': {
                    'presignedURLs': [
                        {
                            'file': 'structures.zip',
                            'URL': url_s3_bucket,
                        },
                        ],
                },
            }

        mocker.post(
            'https://platform.exabyte.io:443/api/2018-10-01/jobs/presigned-urls',
            json=jobs_presigned_urls_json_response,
            status_code=200)

        job = Job("External Job", os.path.join(FIXTURES_DIR, "aiida", "test-001"))
        data_handler = get_data_handler('ExabyteRESTFulAPI', job)
        data_handler.handle()
