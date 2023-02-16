from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()


# Тест 1
def test_add_new_pet(name='Даффи', animal_type='собака', age='1', pet_photo='images/beagle6_0.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


# Тест 2
def test_get_all_pets_with_valid_key(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
    num = len(result['pets'])


# Тест 3
def test_add_photo_at_pet(pet_photo='images/beagle6_0.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, api_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(api_key, 'my_pets')
    status, result = pf.add_photo_of_pet(api_key, my_pets['pets'][0]['id'], pet_photo)
    _, my_pets = pf.get_list_of_pets(api_key, 'my_pets')

    assert status == 200
    assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']


# Тест 4
def test_add_pet_with_empty_fields():
    name = ''
    animal_type = ''
    age = ''
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


# Тест 5
def test_get_api_key_with_incorrect_password_and_email(email=invalid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


# Тест 6
def test_delete_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    assert status == 200
    assert pet_id not in my_pets.values()


# Тест 7
def test__update_pet_info(name='Даффи', animal_type='собака', age=14):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['name'] == name


# Тест 8
def test_get_api_key_with_corr_mail_and_incorr_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


# Тест 9
def test_get_api_key_with_incorr_mail_and_corr_password(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


# Тест 10
def test__delete_pet_with_invalid_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    auth_key = {'key': 'asdasdasdasdadadad34534534534'}
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    assert status == 403
