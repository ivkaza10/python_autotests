import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers', headers={'trainer_token': 'b4c6a01147dcdc83846bb70a931d0a98'} , params={'trainer_id' : 3760})
    assert response.status_code == 200
    assert response.json() ['trainer_name'] == 'Emperor'