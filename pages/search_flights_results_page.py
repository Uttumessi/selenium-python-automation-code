import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class SearchFlightResult(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators :- refactoring just like yatra launch page
    # SEARCH_FLIGHT_RESULTS = "//div[contains(@class, 'stops-details')]//span"
    # FILTER_BY_1_STOPS = "//p[contains(text(),'1')]"
    # FILTER_BY_2_STOPS = "//p[contains(text(),'2')]"
    # FILTER_BY_NON_STOPS = "//p[contains(text(),'0')]"
    #
    # def get_filter_by_1_stop(self):
    #     return self.driver.find_element(By.XPATH, FILTER_BY_1_STOPS)


    def filter_flights(self):
        filter = self.wait_until_element_is_clickable(By.XPATH,"//p[contains(text(),'1')]")
        filter.click()






