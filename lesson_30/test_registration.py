import allure
import pytest
from playwright.sync_api import expect

from core.data.registration_data import (
    ANOTHER_VALID_PASSWORD,
    EMPTY_FIELD_DATA,
    INVALID_FIELD_DATA,
    VALID_PASSWORD,
)

pytestmark = [pytest.mark.ui, allure.epic("UI"), allure.feature("Реєстрація користувача")]


@allure.story("Відкриття форми")
@allure.title("Кнопка 'Sign up' відкриває форму реєстрації")
@allure.description("Перевіряємо, що форма містить усі поля, а Register спочатку неактивна.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive
def test_signup_modal_is_opened(signup_modal):
    signup_modal.is_displayed()

    with allure.step("Кнопка 'Register' неактивна на порожній формі"):
        expect(signup_modal.get_register_button()).to_be_disabled()


@allure.story("Успішна реєстрація")
@allure.title("Реєстрація з валідними даними веде у гараж")
@allure.description("Головний сценарій: валідні дані -> користувач потрапляє у свій гараж.")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.positive
def test_successful_registration(signup_modal, new_user):
    signup_modal.fill_form(
        new_user.name, new_user.last_name, new_user.email, new_user.password
    )

    with allure.step("Кнопка 'Register' стала активною"):
        expect(signup_modal.get_register_button()).to_be_enabled()

    garage_page = signup_modal.click_register()

    garage_page.is_displayed()
    with allure.step("Показано повідомлення 'Registration complete'"):
        expect(garage_page.get_success_alert()).to_have_text("Registration complete")


@allure.story("Email дуплікат")
@allure.title("Повторна реєстрація на існуючий email відхиляється")
@allure.description("Той самий email вдруге не створює другий акаунт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative
def test_registration_with_existing_email(registered_user, main_page):
    signup_modal = main_page.click_sign_up()
    signup_modal.fill_form(
        registered_user.name,
        registered_user.last_name,
        registered_user.email,
        registered_user.password,
    ).try_register()

    with allure.step("Показано помилку 'User already exists'"):
        expect(signup_modal.get_error_alert()).to_have_text("User already exists")

    with allure.step("Форма лишилась відкритою — переходу в гараж не сталося"):
        signup_modal.is_displayed()


@allure.story("Валідація обов'язкових полів")
@allure.title("Порожнє поле '{test_data.field_name}' показує помилку 'required'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
@pytest.mark.parametrize(
    "test_data", EMPTY_FIELD_DATA, ids=lambda d: f"empty_{d.field_name}"
)
def test_empty_required_field(signup_modal, test_data):
    signup_modal.fill_field(test_data.field_name, test_data.value)

    with allure.step(f"Очікуємо текст помилки: {test_data.expected_error}"):
        expect(signup_modal.get_field_error(test_data.field_name)).to_have_text(
            test_data.expected_error
        )

    with allure.step("Кнопка 'Register' лишається неактивною"):
        assert not signup_modal.is_register_enabled()


@allure.story("Валідація значень полів")
@allure.title("Невалідне значення поля '{test_data.field_name}' показує правило валідації")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
@pytest.mark.parametrize(
    "test_data", INVALID_FIELD_DATA, ids=lambda d: f"invalid_{d.field_name}"
)
def test_invalid_field_value(signup_modal, test_data):
    signup_modal.fill_field(test_data.field_name, test_data.value)

    with allure.step(f"Очікуємо текст помилки: {test_data.expected_error}"):
        expect(signup_modal.get_field_error(test_data.field_name)).to_have_text(
            test_data.expected_error
        )

    with allure.step("Кнопка 'Register' лишається неактивною"):
        assert not signup_modal.is_register_enabled()


@allure.story("Валідація значень полів")
@allure.title("Різні паролі блокують реєстрацію")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
def test_passwords_do_not_match(signup_modal, new_user):
    signup_modal.fill_form(
        new_user.name,
        new_user.last_name,
        new_user.email,
        VALID_PASSWORD,
        repeat_password=ANOTHER_VALID_PASSWORD,
    )

    with allure.step("Показано помилку 'Passwords do not match'"):
        expect(signup_modal.get_field_error("repeat_password")).to_have_text(
            ["Passwords do not match"]
        )

    with allure.step("Кнопка 'Register' лишається неактивною"):
        assert not signup_modal.is_register_enabled()


@allure.story("Відкриття форми")
@allure.title("Кнопка 'Register' вмикається лише на повністю заповненій формі")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
def test_register_button_stays_disabled_until_form_is_valid(signup_modal, new_user):
    partial_fields = [
        ("name", new_user.name),
        ("last_name", new_user.last_name),
        ("email", new_user.email),
        ("password", new_user.password),
    ]

    for field_name, value in partial_fields:
        signup_modal.fill_field(field_name, value)
        with allure.step(f"Після поля '{field_name}' кнопка ще неактивна"):
            assert not signup_modal.is_register_enabled()

    signup_modal.fill_field("repeat_password", new_user.repeat_password)
    with allure.step("Форма заповнена повністю — кнопка активна"):
        assert signup_modal.is_register_enabled()
