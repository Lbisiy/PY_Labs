def get_count_char(str_):
    new_str = str_.lower()
    dict_ = {symbol_: new_str.count(symbol_) for symbol_ in new_str if symbol_.isalpha()}  # TODO посчитать количество каждой буквы в строке в аргументе str_
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


#def get_percent_char(str_):
#    new_str = str_.lower()
#    new_str_ = ''.join([symbol_ for symbol_ in new_str if symbol_.isalpha()])
#    dict_ = {symbol_: new_str_.count(symbol_) / len(new_str_) * 100 for symbol_ in new_str_}  # TODO посчитать количество каждой буквы в строке в аргументе str_
#    return dict_

#  print(get_percent_char(main_str))
