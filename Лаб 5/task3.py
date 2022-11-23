import random

def get_unique_list_numbers() -> list[int]:
    list_ = [i for i in range(-10, 11, 1)]
    list__ = random.sample(list_, 15)  # TODO написать функцию для получения списка уникальных целых чисел
    return list__

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
