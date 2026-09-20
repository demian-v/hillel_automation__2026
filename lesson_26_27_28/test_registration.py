import pytest
from playwright.sync_api import expect

from core.data.registration_data import (
    ANOTHER_VALID_PASSWORD,
    EMPTY_FIELD_DATA,
    INVALID_FIELD_DATA,
    VALID_PASSWORD,
)

pytestmark = pytest.mark.ui


@pytest.mark.positive
def test_signup_modal_is_opened(signup_modal):
    """Кнопка 'Sign up' відкриває форму реєстрації з усіма полями."""
    signup_modal.is_displayed()
    expect(signup_modal.get_register_button()).to_be_disabled()


@pytest.mark.positive
def test_successful_registration(signup_modal, new_user):
    """Головний сценарій: валідні дані -> користувач потрапляє у свій гараж."""
    signup_modal.fill_form(
        new_user.name, new_user.last_name, new_user.email, new_user.password
    )
    expect(signup_modal.get_register_button()).to_be_enabled()

    garage_page = signup_modal.click_register()

    garage_page.is_displayed()
    expect(garage_page.get_success_alert()).to_have_text("Registration complete")


@pytest.mark.negative
def test_registration_with_existing_email(registered_user, main_page):
    """Повторна реєстрація на той самий email не створює другий акаунт."""
    signup_modal = main_page.click_sign_up()
    signup_modal.fill_form(
        registered_user.name,
        registered_user.last_name,
        registered_user.email,
        registered_user.password,
    ).try_register()

    expect(signup_modal.get_error_alert()).to_have_text("User already exists")
    # Форма лишилась відкритою — переходу в гараж не сталося
    signup_modal.is_displayed()


@pytest.mark.negative
@pytest.mark.parametrize(
    "test_data", EMPTY_FIELD_DATA, ids=lambda d: f"empty_{d.field_name}"
)
def test_empty_required_field(signup_modal, test_data):
    """Порожнє обов'язкове поле показує повідомлення 'required'."""
    signup_modal.fill_field(test_data.field_name, test_data.value)

    expect(signup_modal.get_field_error(test_data.field_name)).to_have_text(
        test_data.expected_error
    )
    assert not signup_modal.is_register_enabled()


@pytest.mark.negative
@pytest.mark.parametrize(
    "test_data", INVALID_FIELD_DATA, ids=lambda d: f"invalid_{d.field_name}"
)
def test_invalid_field_value(signup_modal, test_data):
    """Невалідне значення поля показує відповідне правило валідації."""
    signup_modal.fill_field(test_data.field_name, test_data.value)

    expect(signup_modal.get_field_error(test_data.field_name)).to_have_text(
        test_data.expected_error
    )
    assert not signup_modal.is_register_enabled()


@pytest.mark.negative
def test_passwords_do_not_match(signup_modal, new_user):
    """Різні паролі блокують реєстрацію."""
    signup_modal.fill_form(
        new_user.name,
        new_user.last_name,
        new_user.email,
        VALID_PASSWORD,
        repeat_password=ANOTHER_VALID_PASSWORD,
    )

    expect(signup_modal.get_field_error("repeat_password")).to_have_text(
        ["Passwords do not match"]
    )
    assert not signup_modal.is_register_enabled()


@pytest.mark.negative
def test_register_button_stays_disabled_until_form_is_valid(signup_modal, new_user):
    """Кнопка 'Register' вмикається лише коли заповнені всі поля."""
    signup_modal.fill_field("name", new_user.name)
    assert not signup_modal.is_register_enabled()

    signup_modal.fill_field("last_name", new_user.last_name)
    assert not signup_modal.is_register_enabled()

    signup_modal.fill_field("email", new_user.email)
    assert not signup_modal.is_register_enabled()

    signup_modal.fill_field("password", new_user.password)
    assert not signup_modal.is_register_enabled()

    signup_modal.fill_field("repeat_password", new_user.repeat_password)
    assert signup_modal.is_register_enabled()
