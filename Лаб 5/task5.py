import random
import string

def get_random_password(n: int=8) -> str:
    str_password = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.sample(str_password, k=n))
  # TODO написать функцию генерации случайных паролей


print(get_random_password())
