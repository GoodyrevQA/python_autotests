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

