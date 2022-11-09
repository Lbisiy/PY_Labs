# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

def list_of_dict(n: int=15) -> None:
    n = 15
    num = [i for i in range(0, n+1)]
    dict_ = {'bin': 0, 'dec': 0, 'hex': 0, 'oct': 0}
    list_ = []

    for n in range(len(num)):
        dict_['bin'] = bin(n)
        dict_['dec'] = n
        dict_['hex'] = hex(n)
        dict_['oct'] = oct(n)
        list_.append(str(dict_))

    return pprint(list_)

list_of_dict()
