from logic_new import *

PLAYER_1 = True
INDEX = 3  # задаем кол-во строк и столбцов поля
field = [' '] * pow(INDEX, 2)  # инициализируем пустое поле

draw_field(field)  # рисуем пустое поле

while True:
    if PLAYER_1 == True:
        while True:
            move = int(input('Чтобы поставить "Х" укажите номер ячейки:'))
            if move > pow(INDEX, 2) or move < 0:
                print('Вы ввели неправильный номер ячейки')
                continue
            else:
                break
        field = player1_step(field, move)
        draw_field(field)
        win = who_win(field)
        continue_ = game_continue(win, move)
        if win != 0 or continue_ != 0:
            break
    else:
        while True:
            move = int(input('Чтобы поставить "0" укажите номер ячейки:'))
            if move > pow(INDEX, 2) or move < 0:
                print('Вы ввели неправильный номер ячейки')
                continue
            else:
                break
        field = player2_step(field, move)
        draw_field(field)
        win = who_win(field)
        continue_ = game_continue(win, move)
        if win != 0 or continue_ != 0:
            break
    PLAYER_1 = not PLAYER_1
