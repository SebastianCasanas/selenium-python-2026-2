from selenium.webdriver.common.by import By
from .base_page import BasePage


class LobbyLoginPage(BasePage):
    URL = "https://lobby-global.vercel.app/"
    USERNAME_FIELD = (By.ID, "username")
    LOGIN_BUTTON = (By.ID, "btn-login")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def open(self):
        self.driver.get(self.URL)

    def join(self, name):
        self.enter_text(self.USERNAME_FIELD, name)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    def is_error_displayed(self):
        return self.find_element(self.ERROR_MESSAGE).is_displayed()

    def is_still_on_login_page(self):
        return self.find_element(self.LOGIN_BUTTON).is_displayed()
