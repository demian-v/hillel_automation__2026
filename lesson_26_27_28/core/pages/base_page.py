from abc import ABC, abstractmethod

from playwright.sync_api import Page


class BasePage(ABC):
    """Спільна основа для всіх сторінок та модальних вікон."""

    def __init__(self, page: Page):
        self.page = page
        # Спливаючі повідомлення (toast) — спільні для всього застосунку.
        # Успішний і помилковий можуть співіснувати, тому адресуємо їх окремо.
        self._success_alert = page.locator(".alert-success")
        self._error_alert = page.locator(".alert-danger")

    @abstractmethod
    def is_displayed(self):
        """Перевірити, що сторінка/компонент відображається."""

    def get_success_alert(self):
        return self._success_alert

    def get_error_alert(self):
        return self._error_alert
