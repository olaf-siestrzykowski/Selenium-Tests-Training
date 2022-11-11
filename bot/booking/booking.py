from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as cons
import os


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium_driver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(cons.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Wybierz walutę"]')
        currency_element.click()
        selected_element = self.find_element(By.CSS_SELECTOR,
                                             f'a[data-modal-header-async-url-param*="changed_currency=1&selected_currency={currency}"]')
        selected_element.click()

    def select_place(self, place):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear()
        search_field.send_keys(place)
        first_result = self.find_element(By.XPATH,
                                         "//div[text()='Amsterdam']")
        first_result.click()

    def select_dates(self, check_in, check_out):
        check_in = self.find_element(By.CSS_SELECTOR,
                                     f'td[span[data-date="{check_in}"]]')
        check_in.click()
        check_out = self.find_element(By.CSS_SELECTOR,
                                      f'td[span[data-date="{check_out}"]]')
        check_out.click()
