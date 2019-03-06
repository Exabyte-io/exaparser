import os

from src.job import Job
from src.utils import read_json
from tests.enums import FIXTURES_DIR
from tests.integration import IntegrationTestBase


class TestJobParser(IntegrationTestBase):

    def setUp(self):
        super(TestJobParser, self).setUp()

    def tearDown(self):
        super(TestJobParser, self).setUp()

    def _clean_job_config(self, config):
        config["workDir"] = ""
        config["workflow"]["subworkflows"][0]["units"][0]["statusTrack"][0]["trackedAt"] = 1551481695

    def test_espresso_001_shell_job(self):
        """
        Extracts a job from an espresso calculation and asserts the results.
        """
        config = Job("External Job", os.path.join(FIXTURES_DIR, "espresso/test-001")).to_json()
        self._clean_job_config(config)
        self.assertDeepAlmostEqual(config, read_json(os.path.join(FIXTURES_DIR, "espresso", "shell-job.json")))

    def test_vasp_001_shell_job(self):
        """
        Extracts a job from a vasp calculation and asserts the results.
        """
        config = Job("External Job", os.path.join(FIXTURES_DIR, "vasp/test-001")).to_json()
        self._clean_job_config(config)
        self.assertDeepAlmostEqual(config, read_json(os.path.join(FIXTURES_DIR, "vasp", "shell-job.json")))
