def check_move(current_player: str, INDEX: int, field: list) -> int:
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
    print(field[0], '|', end=' ')
    print(field[1], '|', end=' ')
    print(field[2])
    print('---------')

    print(field[3], '|', end=' ')
    print(field[4], '|', end=' ')
    print(field[5])
    print('---------')

    print(field[6], '|', end=' ')
    print(field[7], '|', end=' ')
    print(field[8])

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
    :param move: Введенный игроками номер клетки поля от 0 до 8
    :return: 0 - игра продолжается, 1 - игра окончена
    """
    if win == 0 and move != 10:
        continue_ = 0
        print(f'Игра продолжается: {continue_}')
        return continue_
    elif win != 0 or move == 10:
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

