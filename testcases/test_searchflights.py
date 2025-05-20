import time
import pytest
import ddt

from ddt import ddt, data, unpack, file_data

from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResult
from utilities.utils import Utils




@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter():


#57 # @pytest.fixture(autouse=True)
    # def class_setup(self):
    #     self.lp = LaunchPage(self.driver)
    #     self.ut = Utils()

    @data(("New Delhi", "New York", "25", "June 2025"), ("Mumbai", "Chennai", "15", "July 2"))
    @unpack
    @file_data("../testdata/testdata.json")     # test data from json
    @file_data("../testdata/testyml.yaml")     # test data from yaml
    @data(*Utils.read_data_from_excel("D:\\Python Selenium\\TestFrameworkDemo\\testdata\\Book1.xlsx", "Sheet1"))   # test data from excel.
    @data(*Utils.read_data_from_csv("D:\\Python Selenium\\TestFrameworkDemo\\testdata\\test.csv"))   # test data from csv.
    def test_search_flights(self):
        lp = LaunchPage(self.driver)
        # Launching browser and opening the travel website.
        # Dismiss the login popup by clicking somewhere on the page.

#56   # search_flight_result = lp.searchFlights("New Delhi", "New york", "25", "June 2025") # when next page is inside the single func having trigger point.

        lp.searchFlights("New Delhi", "New york", "25", "June 2025") # doing below 4 sepearate fnction calling in single line.

        # Provide going from Location.
        # lp.depart_from("New Delhi")
        # lp.enterDepertFromLocation("New Delhi")   When we define the Locators outside the function

        # # Provide going to Location.
        # lp.going_to("New York")

        # # To Resolve syncronization issue.
        # # Select Departure Date.
        # lp.select_date("22","August 2025")
        # # Click Flight Search Button.
        # lp.click_search()

        # To handle dynamic scroll
        lp.page_scroll()
        # select the filter 1 stop
        sf = SearchFlightResult(self.driver)
        sf.filter_flights()

        # Verify that filtered results show flights having only 1 stop.

#56   # search_flight_result = same for search_flight page (we didn't have the code).

        allstops1 = lp.wait_for_presense_of_all_elements(By.XPATH,"//div[contains(@class, 'stops-details')]//span")
        print(len(allstops1))

        ut = Utils()
        ut.assertlistitems(allstops1, "1 Stop")


        # for stop in allstops1:
        #     stop_text = stop.text.strip()
        #     print("The text is: " + stop_text)
        #
        #     if stop_text.startswith("1 Stop"):
        #         print("assert pass")
        #     else:
        #         print("FAILED")
        #         assert False, f"Unexpected stop value: {stop_text}"




