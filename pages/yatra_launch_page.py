
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from base.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightResult

class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#53 #  LOCATORS :- we have to define all locators like this to maintain the code and easy to reuse and for future updates.
    # the demo below commented function.
    # DEPART_FROM_FIELD = "//div[@aria-label='Departure From New Delhi inputbox']"
    # DEPART_FROM_INPUT = "//div[contains(@class, 'MuiInputBase-root')]//input"
    # FIRST_SUGGESTION_BOX = "//div[contains(@class, 'MuiBox-root')]"

    # def getDepartFromLocation(self):
    #     return self.wait_until_element_is_clickable(By.XPATH , self.DEPART_FROM_FIELD)
# REFACTORING :-
    # def enterDepertFromLocation(self, departlocation):
    #     input_field = self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_INPUT)
    #     input_field.clear()
    #     input_field.send_keys(departlocation)
    #     time.sleep(2)
    #     first_suggestion = self.wait_until_element_is_clickable(By.XPATH, self.FIRST_SUGGESTION_BOX)
    #     first_suggestion.click()

    def depart_from(self, departlocation):
        departure_section = self.wait_until_element_is_clickable(By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']")
        departure_section.click()
        time.sleep(1)
        # Now interact with the actual input field
        input_field = self.wait_until_element_is_clickable(By.XPATH,"//div[contains(@class, 'MuiInputBase-root')]//input")
        input_field.clear()
        input_field.send_keys(departlocation)
        time.sleep(2)
        first_suggestion = self.wait_until_element_is_clickable(By.XPATH, "//div[contains(@class, 'MuiBox-root')]")
        first_suggestion.click()


    def going_to(self, goingtolocation):
        to_section = self.wait_until_element_is_clickable(By.XPATH, "//div[contains(@aria-label,'Going To Mumbai inputbox')]")
        to_section.click()
        time.sleep(1)
        to_input = self.wait_until_element_is_clickable(By.XPATH, "//div[contains(@class, 'MuiInputBase-root')]//input")
        to_input.clear()
        to_input.send_keys(goingtolocation)
        time.sleep(2)
        second_suggestion = self.wait_until_element_is_clickable(By.XPATH,  "//div[contains(@class, 'MuiBox-root')]")
        second_suggestion.click()
        time.sleep(2)

    def select_date(self, desired_day, desired_month_year):
        # Step 1: Open the date picker calendar
        try:
            # Wait for date picker to be clickable
            date_picker = self.wait_until_element_is_clickable(By.XPATH, "//div[@aria-label='Departure Date inputbox']")
            date_picker.click()
            time.sleep(3)  # Wait a bit for the calendar to load
        except TimeoutException as e:
            print(f"Error: Date picker not clickable - {e}")
            return

        # Step 2: Navigate to the desired month and year
        for _ in range(12):
            try:
                # Wait for the calendar's month and year header to load
                month_year_element = self.wait_for_presense_of_element(
                    By.XPATH, "//div[contains(@class, 'MuiPickersCalendarHeader-label')]"
                )
                current_month_year = month_year_element.text.strip()

                # Check if we found the desired month and year
                if current_month_year == desired_month_year:
                    break

                # If not, click the 'next month' button
                next_button = self.wait_until_element_is_clickable(By.XPATH, "//button[@aria-label='Next month']")
                next_button.click()
                time.sleep(3)  # Give time for the next month to load
            except TimeoutException as e:
                print(f"Error: Failed to find or click next month button - {e}")
                return

        else:
            print(f"Error: Could not find the month {desired_month_year}")
            return

        # Step 3: Select the desired day from the calendar
        try:
            # Find all available dates in the calendar
            all_dates = self.driver.find_elements(By.XPATH,
                                                  "//div[contains(@aria-label,'Choose') and normalize-space(text()) != '']")

            # Loop through and select the desired date
            for date in all_dates:
                if date.text.strip() == desired_day:
                    date.click()
                    break
            time.sleep(2)
        except TimeoutException as e:
            print(f"Error: Failed to select date - {e}")
            return

    def click_search(self):
        search_button = self.wait_until_element_is_clickable(By.XPATH, "//button[normalize-space()='Search']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
        time.sleep(1)  # optional wait
        self.driver.execute_script("arguments[0].click();", search_button)


    def searchFlights(self, departlocation, goingtolocation, desired_day, desired_month_year):
        self.depart_from(departlocation)
        self.going_to(goingtolocation)
        self.select_date(desired_day, desired_month_year)
        self.click_search()
#56    # search_result_flight = SearchFlightResult(self.driver) # we don't have to create object of next page in test.
       # return search_result_flight