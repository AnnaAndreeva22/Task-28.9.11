import pytest
import json
import requests
from pydantic import BaseModel
from settings import key, wrong_key, wrong_id

class GetApiKey(BaseModel):
    email = str
    password = str


def test_get_api_key():

    url = 'https://petfriends.skillfactory.ru/api/key'
    headers = {"email": "anna****.ru", "password": "pet****"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    result = response.json()
    assert response.json()


class Pet(BaseModel):
    name = str
    animal_type = str
    age = int
    pet_id = str
    filter = str

def test_create_pet_simple():

    url = 'https://petfriends.skillfactory.ru/api/create_pet_simple'
    data = {'name': 'Bobik', 'animal_type': 'rabbit', 'age': 6}
    headers = {'auth_key': key}

    response = requests.post(url, headers=headers, data=data)

    assert response.status_code == 200


def test_create_pet_simple_with_invalid_key():

    url = 'https://petfriends.skillfactory.ru/api/create_pet_simple'
    data = {'name': 'Bobik', 'animal_type': 'rabbit', 'age': 6}
    headers = {'auth_key': wrong_key}

    response = requests.post(url, headers=headers, data=data)

    assert response.status_code == 403
    print('Use correct auth_key')


def test_update_pet_with_wrong_id():

    url = 'https://petfriends.skillfactory.ru/api/pets/ + wrong_id'
    headers = {'auth_key': key}
    data = {'name': 'Frankie', 'animal_type': 'cat', 'age': 4}

    response = requests.put(url, headers=headers, data=data)

    assert response.status_code == 400
    print('Use correct id')



def test_get_list_of_pets():

    url = 'https://petfriends.skillfactory.ru/api/pets'
    headers = {'auth_key': key}
    filter = {'filter': "my_pets"}

    response = requests.get(url, headers=headers, params=filter)


    assert response.status_code == 200
    result = response.json()
    assert len(result['pets']) > 0
    print('Number of my pets:', len(result['pets']))
    assert result

