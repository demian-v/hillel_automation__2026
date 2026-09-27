import platform
import sys
from pathlib import Path

import allure
import pytest

from core.config import BASE_URL, BASIC_AUTH_PASSWORD, BASIC_AUTH_USER
from core.data.registration_data import generate_new_user
from core.pages.main_page import MainPage


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


@pytest.fixture(scope="session", autouse=True)
def allure_environment_file(pytestconfig):
    """Заповнити блок ENVIRONMENT у звіті Allure."""
    results_dir = Path(pytestconfig.getoption("--alluredir") or "allure-results")
    results_dir.mkdir(parents=True, exist_ok=True)
    (results_dir / "environment.properties").write_text(
        "\n".join([
            f"Base.URL={BASE_URL}",
            f"Browser={pytestconfig.getoption('--browser') or ['chromium']}",
            f"Headless={not pytestconfig.getoption('--headed')}",
            f"Python={sys.version.split()[0]}",
            f"Platform={platform.platform()}",
        ]),
        encoding="utf-8",
    )


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
    user = generate_new_user()
    # Дані видно у звіті — зручно, коли тест впав на конкретному email
    allure.attach(
        f"name: {user.name}\nlast name: {user.last_name}\nemail: {user.email}",
        name="Тестовий користувач",
        attachment_type=allure.attachment_type.TEXT,
    )
    return user


@pytest.fixture
def registered_user(signup_modal, new_user):
    """Вже зареєстрований користувач (сесію закрито) — для перевірки дубля email."""
    with allure.step("Передумова: зареєструвати користувача і вийти з акаунта"):
        garage_page = signup_modal.fill_form(
            new_user.name, new_user.last_name, new_user.email, new_user.password
        ).click_register()
        garage_page.is_displayed()
        garage_page.log_out().is_displayed()
    return new_user


@pytest.fixture(autouse=True)
def allure_environment(request):
    """Посилання на стенд у кожному тесті."""
    allure.dynamic.link(BASE_URL, name="Тестовий стенд qauto2")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # Скріншот і URL чіпляємо прямо до звіту Allure — шукати файли не треба
            allure.attach(
                page.screenshot(full_page=True),
                name=f"screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                page.url, name="URL на момент падіння",
                attachment_type=allure.attachment_type.TEXT,
            )
