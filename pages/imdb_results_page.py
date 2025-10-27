from selenium.webdriver.common.by import By
from pages.base_page import BasePage

MOVIE_LINK = (By.CLASS_NAME, "ipc-metadata-list-summary-item__t")


class ImdbResultsPage(BasePage):
    def click_movie_name(self):
        self.click(MOVIE_LINK)

