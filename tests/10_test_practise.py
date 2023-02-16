from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()


# Тест 1

# Тест 2
# Тест 3
# Тест 4
# Тест 5
def test_get_api_key_with_correct_mail_and_incorrect_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
    print('ok')
    print(f'Статус {status} для теста с неправильным паролем')
# Тест 6
# Тест 7
# Тест 8
# Тест 9
# Тест 10
