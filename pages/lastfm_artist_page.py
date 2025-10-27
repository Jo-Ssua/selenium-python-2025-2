from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ArtistPage(BasePage):
    LAST_RELEASE_DATE = (By.CLASS_NAME, "artist-header-featured-items-item-date")

    def get_last_release_date(self):
        return self.find_element(self.LAST_RELEASE_DATE).text