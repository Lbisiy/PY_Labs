def check_move(current_player: str, INDEX: int, field: list) -> int:
    """
    Функция проверок ходов игроков (правильная/неправильная, занята/не занята)
    :param current_player: 'крестик' или 'нолик'
    :param INDEX: Размерность поля
    :param field: Инициализированное поле с ходами игроков в виде list
    :return: Ход игрока для размещения на поле
    """
    while True:
        move = int(input(f'Чтобы поставить {current_player} укажите номер ячейки:'))
        if move > pow(INDEX, 2) or move < 0:
            print('Вы ввели неправильный номер ячейки')
            continue
        elif field[move-1] == 'X' or field[move-1] == '0':
            print('Ячейка занята!')
        else:
            break
    return move

def draw_field(field: list) -> None:
    """
    Функция отрисовки поля
    Поле фиксированного размера 3х3

    :param field: Подается на вход изначально заданный пустой list, а затем иземенный list после ходов игроков
    :return None: Печатает начальное и поле после каждого хода
    """
    for i, value in enumerate(field):
        print(' |', value, end='')
        if i == 2 or i == 5 or i == 8:
            print(' |')
            print('---------------')
            continue

def who_win(field: list) -> int:
    """
    Функция проверки победы
    :param field: Поле после хода игрока
    :return win: Возвращает 1-первый игрок выиграл, 2-второй, 0-никто
    """
    if field[0] == field[1] == field[2] == 'X' or field[3] == field[4] == field[5] == 'X' or \
        field[6] == field[7] == field[8] == 'X' or field[0] == field[3] == field[6] == 'X' or \
        field[1] == field[4] == field[7] == 'X' or field[2] == field[5] == field[8] == 'X' or \
        field[0] == field[4] == field[8] == 'X' or field[2] == field[4] == field[6] == 'X':
        win = 1
        print('Выиграл игрок: 1')
        return win
    elif field[0] == field[1] == field[2] == '0' or field[3] == field[4] == field[5] == '0' or \
        field[6] == field[7] == field[8] == '0' or field[0] == field[3] == field[6] == '0' or \
        field[1] == field[4] == field[7] == '0' or field[2] == field[5] == field[8] == '0' or \
        field[0] == field[4] == field[8] == '0' or field[2] == field[4] == field[6] == '0':
        win = 2
        print('Выиграл игрок: 2')
        return win
    else:
        win = 0
        print('Выиграл игрок: 0')
        return win

def game_continue(win: int, move: int) -> int:
    """
    Функция проверки окончания игры после каждого хода
    :param win: Результат функции проверки победы. 1-первый игрок выиграл, 2-второй, 0-никто
    :param move: Введенный игроками номер клетки поля от 1 до 9
    :return: 0 - игра продолжается, 1 - игра окончена
    """
    if win == 0:
        continue_ = 0
        print(f'Игра продолжается: {continue_}')
        return continue_
    elif win != 0:
        continue_ = 1
        print(f'Игра окончена: {continue_}')
        return continue_


def player_step(field, move, current_player) -> list:
    """
    Функция хода первого игрока. Переводит номер клетки, введенной игроком в "крестик"
    :param field: Поле до хода игрока
    :param move: Введенный номер клетки игроком
    :return: Новое поле после хода игрока
    """
    move_ = move - 1
    for value in field:
        if value == ' ':
            field[move_] = current_player
            return field

