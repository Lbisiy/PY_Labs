from logic_new import *

INDEX = 3  # задаем кол-во строк и столбцов поля
field = [' '] * pow(INDEX, 2)  # инициализируем пустое поле

draw_field(field)  # рисуем пустое поле

current_player = 'X'  #назначаем первого игрока, который ходит 'крестиком'
while True:
    move = check_move(current_player, INDEX, field)
    field = player_step(field, move, current_player)
    draw_field(field)
    win = who_win(field)
    continue_ = game_continue(win, move)
    if win != 0 or continue_ != 0:
        break
    current_player = "X" if current_player == "0" else "0"
