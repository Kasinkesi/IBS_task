from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    WAITING_TIME = 5

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find_elem(self, locator, time=WAITING_TIME):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elems(self, locator, time=WAITING_TIME):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def find_visible_elem(self, locator, time=WAITING_TIME):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_visible_elems(self, locator, time=WAITING_TIME):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")
