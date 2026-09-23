from playwright.sync_api import Page, expect

from core.config import BASE_URL
from core.pages.base_page import BasePage
from core.pages.signup_modal import SignUpModal


class MainPage(BasePage):
    """Головна (лендінгова) сторінка qauto2."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.__logo = page.locator(".header_logo")
        self.__sign_up_button = page.get_by_role("button", name="Sign up")
        self.__sign_in_button = page.locator(".header_signin")
        self.__guest_log_in_button = page.locator(".header-link.-guest")

    def is_displayed(self):
        expect(self.__logo).to_be_visible()
        expect(self.__sign_up_button).to_be_visible()

    def open(self):
        self.page.goto(BASE_URL)
        return self

    def click_sign_up(self) -> SignUpModal:
        self.__sign_up_button.click()
        return SignUpModal(self.page)
