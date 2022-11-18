import random

def get_random_password() -> str:
    password = ''
    list_int = [str(item_) for item_ in range(10)] + [chr(char, ).lower() for char in range(97,123)] + \
               [chr(char).upper() for char in range(97,123)]
    list__ = random.sample(list_int, 8)
    password = ''.join(list__)
    return password
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
