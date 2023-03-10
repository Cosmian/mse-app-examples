import requests


def test_average(url, certificate):
    response = requests.delete(f'{url}/', verify=certificate)
    assert response.status_code == 200

    response = requests.get(f'{url}/', verify=certificate)
    assert response.status_code == 200
    assert response.json() == {"max": None}

    response = requests.post(f'{url}/', json={"n": 100.0}, verify=certificate)
    assert response.status_code == 200

    response = requests.get(f'{url}/', verify=certificate)
    assert response.status_code == 200
    assert response.json() == {"max": 'User #1'}

    response = requests.post(f'{url}/', json={"n": 200.0}, verify=certificate)
    assert response.status_code == 200

    response = requests.get(f'{url}/', verify=certificate)
    assert response.status_code == 200
    assert response.json() == {"max": 'User #2'}

    response = requests.delete(f'{url}/', verify=certificate)
    assert response.status_code == 200

    response = requests.get(f'{url}/', verify=certificate)
    assert response.status_code == 200
    assert response.json() == {"max": None}


def test_average_error(url, certificate):
    response = requests.post(f'{url}/', verify=certificate)
    assert response.status_code == 422

    response = requests.post(f'{url}/', json={"n": "str"}, verify=certificate)
    assert response.status_code == 422


def test_health(url, certificate):
    response = requests.get(f"{url}/health", verify=certificate)
    assert response.status_code == 200
