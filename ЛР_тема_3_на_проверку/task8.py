money_capital = 10000
salary = 5000
spend = spend_cumulative = 6000  # разделяем неизменяемую и с нарастающим приращением
increase = 0.05
budget = salary + money_capital  # переменная для сравнения с тратами
month = 0  # количество месяцев, которое можно прожить
while budget >= spend_cumulative:  # выбираем while, т.к. не знаем кол-во циклов
    spend_cumulative = spend * (1 + increase * month)
    money_capital = money_capital + (salary - spend_cumulative)
    budget = salary + money_capital
    month = month + 1

print(month)
