import logging
import sys
from pathlib import Path

import pytest

# Налаштування серверної частини (cars_app.py)
BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"

# Лог пишемо поряд з тестом, щоб не залежати від того, звідки запущено pytest
LOG_FILE = Path(__file__).parent / "test_search.log"
LOGGER_NAME = "cars_search"

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def pytest_configure(config):
    """Реєструємо маркер локально, щоб не правити кореневий pytest.ini (--strict-markers)."""
    config.addinivalue_line("markers", "cars_api: api tests for local cars_app endpoints")


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """
    Setup: логер з двома хендлерами - консоль (stdout) і файл test_search.log.
    Teardown: закриваємо і знімаємо хендлери, щоб не дублювались при повторних запусках.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("=" * 30 + " START TEST SESSION " + "=" * 30)
    yield logger
    logger.info("=" * 30 + " END TEST SESSION " + "=" * 30)

    for handler in (console_handler, file_handler):
        logger.removeHandler(handler)
        handler.close()
