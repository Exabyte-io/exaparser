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

    def test_espresso_001_shell_job(self):
        config = Job(os.path.join(FIXTURES_DIR, "espresso/test-001")).to_json()
        config["workDir"] = ""
        self.assertDeepAlmostEqual(config, read_json(os.path.join(FIXTURES_DIR, "espresso-001-shell-job.json")))
