import os

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
