def need_money_for_months(months, salary=5000, spend=6000, increase=0.03):
#  salary = 5000  - зарплата
#  spend = 6000   - траты
#  months = 10  - количество месяцев
#  increase = 0.03  - рост цен
    need_money = 0  # количество денег, чтобы прожить 10 месяцев
    for month in range(1, 2):  # for, т.к. знаем кол-во циклов и делаем 1 цикл, в котором не меняется spend
        need_money = need_money - salary + spend
    for month in range(2, months + 1):  # делаем остальные 9 циклов с приращением spend
        spend = spend * (1 + increase)
        need_money = need_money - salary + spend
    print(round(need_money))

need_money_for_months(10)