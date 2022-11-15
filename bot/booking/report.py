from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Report:
    def __init__(self, boxes_section: WebElement):
        self.boxes_section = boxes_section
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_data(self):
        collection = []
        for deal_box in self.deal_boxes:
            name = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip()
            price = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="availability-rate-information"]'
                                          ).find_element(By.CSS_SELECTOR, 'span[aria-hidden="true"]'
                                                         ).get_attribute('innerHTML').strip()
            price = price.replace('&nbsp;', ' ')
            '''distance = deal_box.find_element(By.CSS_SELECTOR, 'span[data-testid="distance"]'
                                             ).get_attribute('innerHTML').strip()'''
            rating = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]'
                                           ).find_element(By.CSS_SELECTOR, 'div').get_attribute('innerHTML').strip()
            collection.append([name, price, rating])
        return collection
