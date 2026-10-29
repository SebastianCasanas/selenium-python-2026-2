from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class ImdbHomePage(BasePage):
    URL = "https://www.imdb.com/"
    SEARCH_INPUT = (By.ID, "suggestion-search")
    VERIFICATION_TIMEOUT = 120

    def open(self):
        self.driver.get(self.URL)
        # IMDb puede mostrar "Human Verification": se resuelve a mano en la ventana de Chrome
        WebDriverWait(self.driver, self.VERIFICATION_TIMEOUT).until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )

    def search(self, text):
        self.enter_text(self.SEARCH_INPUT, text)
        self.find_element(self.SEARCH_INPUT).send_keys(Keys.ENTER)
