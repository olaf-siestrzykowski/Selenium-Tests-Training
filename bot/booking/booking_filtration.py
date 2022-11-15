from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def sorting(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid = "sorters-dropdown-trigger"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-id = "price"]').click()

    def star_rating(self, *stars):
        star_div = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_child_elements = star_div.find_elements(By.CSS_SELECTOR, '*')

        for star in stars:
            for child in star_child_elements:
                star_str = str(child.get_attribute('innerHTML')).strip()
                if star_str == f'{star} gwiazdki' or star_str == f'{star} gwiazdek' or star_str == f'{star} gwiazdka':
                    child.click()
