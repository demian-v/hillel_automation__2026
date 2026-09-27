import allure
from playwright.sync_api import Page, expect

from core.pages.base_page import BasePage
from core.pages.garage_page import GaragePage


class SignUpModal(BasePage):
    """Модальне вікно 'Registration'."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.__modal = page.locator("app-signup-modal")
        self.__title = self.__modal.locator(".modal-title")

        self.__name = page.locator("#signupName")
        self.__last_name = page.locator("#signupLastName")
        self.__email = page.locator("#signupEmail")
        self.__password = page.locator("#signupPassword")
        self.__repeat_password = page.locator("#signupRepeatPassword")

        self.__register_button = self.__modal.locator(".modal-footer button.btn-primary")

        # Поля у порядку появи у формі — потрібно, щоб адресувати помилку конкретного поля
        self.__fields = {
            "name": self.__name,
            "last_name": self.__last_name,
            "email": self.__email,
            "password": self.__password,
            "repeat_password": self.__repeat_password,
        }

    @allure.step("Перевірити, що форма реєстрації відкрита")
    def is_displayed(self):
        expect(self.__modal).to_be_visible()
        expect(self.__title).to_have_text("Registration")
        for field in self.__fields.values():
            expect(field).to_be_visible()

    def get_register_button(self):
        return self.__register_button

    @allure.step("Заповнити поле '{field_name}' значенням '{value}'")
    def fill_field(self, field_name: str, value: str):
        """Заповнити одне поле та зняти з нього фокус, щоб спрацювала валідація."""
        field = self.__fields[field_name]
        field.fill(value)
        field.blur()
        return self

    @allure.step("Заповнити форму реєстрації")
    def fill_form(self, name, last_name, email, password, repeat_password=None):
        values = {
            "name": name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "repeat_password": password if repeat_password is None else repeat_password,
        }
        for field_name, value in values.items():
            if value is not None:
                self.fill_field(field_name, value)
        return self

    def get_field_error(self, field_name: str):
        """Локатори рядків помилки у form-group конкретного поля.

        Одна помилка може складатись з кількох <p>, тому повертаємо саме їх,
        а не контейнер .invalid-feedback.
        """
        return (
            self.__fields[field_name]
            .locator("xpath=..")
            .locator(".invalid-feedback p")
        )

    @allure.step("Перевірити, чи активна кнопка 'Register'")
    def is_register_enabled(self) -> bool:
        return self.__register_button.is_enabled()

    @allure.step("Натиснути 'Register' (очікуємо успіх)")
    def click_register(self) -> GaragePage:
        """Успішний сценарій — після реєстрації відкривається гараж."""
        self.__register_button.click()
        return GaragePage(self.page)

    @allure.step("Натиснути 'Register' (очікуємо помилку)")
    def try_register(self):
        """Негативний сценарій — форма лишається відкритою з помилкою."""
        self.__register_button.click()
        return self
