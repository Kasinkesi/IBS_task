import json

from base_page import BasePage
from selenium.webdriver.common.by import By



class MainPageLocators:
    GET_DELAYED_RESPONSE = (By.CSS_SELECTOR, 'li[data-id ="delay"]')
    RESPONSE_CODE = (By.CSS_SELECTOR, '.response-code')
    RESPONSE_OUTPUT = (By.CSS_SELECTOR, 'pre[data-key="output-response"]')


class MainPage(BasePage):
    def click_get_delayed_response(self):
        delayed_response_button = self.find_elem(MainPageLocators.GET_DELAYED_RESPONSE)
        delayed_response_button.click()

    def response_code_number(self):
        response_code_number = int(self.find_elem(MainPageLocators.RESPONSE_CODE).text)
        return response_code_number

    def response_output_json(self):
        response_output = self.find_visible_elem(MainPageLocators.RESPONSE_OUTPUT)
        return json.loads(response_output.text)


