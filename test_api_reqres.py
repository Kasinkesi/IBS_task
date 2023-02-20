import requests

BASE_URL = "https://reqres.in/"


def test_get_list_users():
    url_path = "api/users/"
    params = {"page": 2}
    r = requests.get(BASE_URL + url_path, params=params)
    assert r.status_code == 200
    assert r.json()["page"] == 2


def test_get_single_user():
    url_path = "api/users/"
    user_num = "2"
    r = requests.get(BASE_URL + url_path + user_num)
    assert r.status_code == 200
    assert r.json()["data"]["id"] == 2


def test_get_single_user_not_found():
    url_path = "api/users/"
    user_num = "23"
    r = requests.get(BASE_URL + url_path + user_num)
    assert r.status_code == 404


def test_get_list_resource():
    url_path = "api/unknown/"
    r = requests.get(BASE_URL + url_path)
    assert r.status_code == 200
    assert r.json()["page"] == 1


def test_get_single_resource():
    url_path = "api/unknown/2"
    r = requests.get(BASE_URL + url_path)
    assert r.status_code == 200
    assert r.json()["data"]["id"] == 2


def test_get_single_resource_found():
    url_path = "api/users/"
    resource_num = "23"
    r = requests.get(BASE_URL + url_path + resource_num)
    assert r.status_code == 404


def test_post_creat():
    url_path = "api/users/"
    payload = {"name": "morpheus", "job": "leader"}
    r = requests.post(BASE_URL + url_path, data=payload)
    assert r.status_code == 201
    assert r.json()["name"] == "morpheus"
    assert "createdAt" in r.json()


def test_put_update():
    url_path = "api/users/2"
    payload = {"name": "morpheus", "job": "zion resident"}
    r = requests.put(BASE_URL + url_path, data=payload)
    assert r.status_code == 200
    assert r.json()["name"] == "morpheus"
    assert "updatedAt" in r.json()


def test_patch_update():
    url_path = "api/users/2"
    payload = {"name": "morpheus", "job": "zion resident"}
    r = requests.patch(BASE_URL + url_path, data=payload)
    assert r.status_code == 200
    assert r.json()["name"] == "morpheus"
    assert "updatedAt" in r.json()


def test_delete_delete():
    url_path = "api/users/2"
    r = requests.delete(BASE_URL + url_path)
    assert r.status_code == 204


def test_post_register_successful():
    url_path = "api/register/"
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    r = requests.post(BASE_URL + url_path, data=payload)
    assert r.status_code == 200
    assert r.json()["id"] == 4


def test_post_register_unsuccessful():
    url_path = "api/register/"
    payload = {"email": "sydney@fife"}
    r = requests.post(BASE_URL + url_path, data=payload)
    assert r.status_code == 400
    assert r.json()["error"] == "Missing password"

def test_post_login_successful():
    url_path = "api/login/"
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    r = requests.post(BASE_URL + url_path, data=payload)
    assert r.status_code == 200
    assert r.json()["token"] == "QpwL5tke4Pnpja7X4"

def test_post_login_unsuccessful():
    url_path = "api/login/"
    payload = {"email": "peter@klaven"}
    r = requests.post(BASE_URL + url_path, data=payload)
    assert r.status_code == 400
    assert r.json()["error"] == "Missing password"

def test_get_delayed_response():
    url_path = "api/users/"
    params = {"delay": 3}
    r = requests.get(BASE_URL + url_path, params=params)
    assert r.status_code == 200
    assert r.json()["page"] == 1

