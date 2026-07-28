import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from hillel_automation__2026.lesson_13.homework_13 import log_event

LOG_FILE = "login_system.log"

def read_log_lines():
    with open(LOG_FILE) as f:
        content = f.read()
    return content.splitlines()

class TestHomework13(unittest.TestCase):

    def test_success(self):
        log_event("Demian", "success")

        actual_result = read_log_lines()[-1]
        self.assertIn("Login event - Username: Demian, Status: success - INFO", actual_result)

    def test_expired(self):
        log_event("Alex", "expired")

        actual_result = read_log_lines()[-1]
        self.assertIn("Login event - Username: Alex, Status: expired - WARNING", actual_result)

    def test_failed(self):
        log_event("Frank", "failed")

        actual_result = read_log_lines()[-1]
        self.assertIn("Login event - Username: Frank, Status: failed - ERROR", actual_result)