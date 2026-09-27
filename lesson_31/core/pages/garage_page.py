import allure
from playwright.sync_api import Page, expect

from core.config import GARAGE_URL
from core.pages.base_page import BasePage


class GaragePage(BasePage):
    """Сторінка 'Garage' — куди потрапляє користувач після реєстрації."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.__heading = page.get_by_role("heading", name="Garage")
        self.__add_car_button = page.get_by_role("button", name="Add car")
        # Меню користувача у шапці — не ховається на вузьких вікнах, на відміну від сайдбару
        self.__user_nav = page.locator("#userNavDropdown")
        self.__log_out_button = page.get_by_role("button", name="Logout")

    @allure.step("Перевірити, що відкрилась сторінка 'Garage'")
    def is_displayed(self):
        expect(self.page).to_have_url(GARAGE_URL)
        expect(self.__heading).to_be_visible()
        expect(self.__add_car_button).to_be_visible()

    @allure.step("Вийти з акаунта")
    def log_out(self):
        """Вийти з акаунта і повернутись на головну сторінку."""
        self.__user_nav.click()
        self.__log_out_button.click()
        from core.pages.main_page import MainPage

        return MainPage(self.page)
