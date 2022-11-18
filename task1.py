# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

def list_of_dict(n: int=15) -> None:
    n = 15
    list_ = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(n+1)]
    return pprint(list_)

list_of_dict()


