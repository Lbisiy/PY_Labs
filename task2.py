def get_count_char(main_str):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    main_str = main_str.lower()
    str_dict = {}
    count_value = 0
    for value in main_str:
        if value.isalpha():
            if value in str_dict.keys():
                str_dict[value] += 1
            else:
                str_dict[value] = 1
    return str_dict

def get_count_percent(str_dict):
    new_str_dict = {}
    total_count = sum(str_dict.values())
    for key, value in str_dict.items():
        percent_value = round((value / total_count) * 100, 2)
        new_str_dict[key] = percent_value
    return new_str_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_count_percent(get_count_char(main_str)))
