import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Remote(
    #     command_executor='http://localhost:4444',
    #     desired_capabilities={'browserName': 'chrome'})
    yield driver
    driver.quit()
