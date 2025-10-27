from selenium.webdriver.common.by import By
from pages.base_page import BasePage

SEARCH_INPUT = (By.ID, "suggestion-search")
SEARCH_BUTTON = (By.ID, "suggestion-search-button")

class ImdbHomePage(BasePage):
    def search_movie(self, movie_name):
        self.enter_text(SEARCH_INPUT, movie_name)
        self.click(SEARCH_BUTTON)
