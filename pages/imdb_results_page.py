from selenium.webdriver.common.by import By
from .base_page import BasePage


class ImdbResultsPage(BasePage):
    FIRST_TITLE_RESULT = (By.XPATH, "(//section[@data-testid='find-results-section-title']//a[contains(@href, '/title/')])[1]")

    def open_first_result(self):
        self.click(self.FIRST_TITLE_RESULT)
