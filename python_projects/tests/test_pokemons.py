import requests
import pytest
import json

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_is_in_response():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id' : "1825"})
    assert response.json()['trainer_name'] == "GooD"

@pytest.mark.parametrize('key, value', [('trainer_name', 'GooD'),('city', 'Moscow'), ('level', '5')])

def test_params(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : "1825"})
    assert response.json()[key] == value

