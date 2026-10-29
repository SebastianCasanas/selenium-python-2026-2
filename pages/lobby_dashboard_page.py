from selenium.webdriver.common.by import By
from .base_page import BasePage


class LobbyDashboardPage(BasePage):
    USERNAME = (By.CLASS_NAME, "participant-name")

    def is_user_in_lobby(self, name):
        locator = (By.XPATH, f"//span[@class='participant-name' and text()='{name}']")
        return self.find_element(locator).is_displayed()
