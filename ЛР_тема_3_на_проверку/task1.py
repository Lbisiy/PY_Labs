src = not False and True or False and not True

src = True and True or False and False  # избавляемся от not
src = True or False  # избавляемся от and
src = True  # избавляемся от or
# TODO расписать упрощение выражения

result = True

print(src == result)
