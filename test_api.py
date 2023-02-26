import requests
import pytest

def test_statuscode():
    response = requests.get('https://swapi.dev/api/people/3')
    assert response.status_code == 200

def test_peace_of_body():
    response = requests.get('https://swapi.dev/api/people/3')
    assert response.json()['name'] == 'R2-D2'

@pytest.mark.parametrize("key, value, id", [('name', 'R2-D2', 3), ('name', 'Darth Vader', 4), ('name', 'Luke Skywalker', 1)])
def test_body(key, value, id):
    response = requests.get(f'https://swapi.dev/api/people/{id}')
    assert response.json()[key] == value

def test_agent():
    url_token = "https://partner.agentapp.ru/v1/users/obtain-token"
    response = requests.post(url_token, json={
        "username":"qa@qa.qa",
        "password":111
    })
    token_app = response.json()['token']
    url_driver = "https://partner.agentapp.ru/v1/insured_objects/drivers"
    response2 = requests.post(url_driver, json={
        "first_name": "Иван",
        "last_name": "Иванов",
        "patronymic": "Иванович",
        "birth_date": "1987-10-10",
        "driving_expirience_started": "2010-01-01",
        "driver_licenses": [{"credential_type": "DRIVER_LICENSE",
                             "number": "012345",
                             "series": "1234",
                             "issue_date": "2010-01-01"}]

    }, headers={"Authorization":f"Token {token_app}"})

    assert response2.status_code == 201
