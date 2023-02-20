import time

import requests
from reqres_page import MainPage
import pytest

BASE_URL = "https://reqres.in/"


@pytest.mark.parametrize("delay_time", ("0", "3", "-1"))
def test_get_delayed_response(browser, delay_time):
    # api response
    url_path = "api/users/"
    params = {"delay": delay_time}
    api_response = requests.get(BASE_URL + url_path, params=params)
    # web response
    main_page = MainPage(browser, BASE_URL)
    main_page.open()
    main_page.click_get_delayed_response()
    response_code = main_page.response_code_number()
    time.sleep(abs(int(delay_time)))
    response_output = main_page.response_output_json()

    assert response_code == api_response.status_code
    assert response_output == api_response.json()
