from pathlib import Path

import pytest

from core.config import BASIC_AUTH_PASSWORD, BASIC_AUTH_USER
from core.data.registration_data import generate_new_user
from core.pages.main_page import MainPage

SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    # Режимом headless/headed керує прапорець pytest --headed
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig):
    # Стенд закритий basic-auth, тому логін/пароль віддаємо на рівні контексту
    args = {
        **browser_context_args,
        "http_credentials": {
            "username": BASIC_AUTH_USER,
            "password": BASIC_AUTH_PASSWORD,
        },
    }
    if pytestconfig.getoption("--headed"):
        # Вікно на весь екран — розмір бере з --start-maximized
        args["no_viewport"] = True
    else:
        # У headless розмір задаємо явно, щоб верстка не "з'їжджала"
        args["viewport"] = {"width": 1920, "height": 1080}
    return args


@pytest.fixture
def main_page(page) -> MainPage:
    """Відкрита головна сторінка."""
    return MainPage(page).open()


@pytest.fixture
def signup_modal(main_page):
    """Відкрите модальне вікно реєстрації — стартова точка більшості тестів."""
    return main_page.click_sign_up()


@pytest.fixture
def new_user():
    """Унікальні дані нового користувача для кожного тесту."""
    return generate_new_user()


@pytest.fixture
def registered_user(signup_modal, new_user):
    """Вже зареєстрований користувач (сесію закрито) — для перевірки дубля email."""
    garage_page = signup_modal.fill_form(
        new_user.name, new_user.last_name, new_user.email, new_user.password
    ).click_register()
    garage_page.is_displayed()
    garage_page.log_out().is_displayed()
    return new_user


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            SCREENSHOTS_DIR.mkdir(exist_ok=True)
            page.screenshot(path=str(SCREENSHOTS_DIR / f"{item.name}.png"))
