import random
from typing import List


def check_move(current_player: str, index: int, field: List[str]) -> int:
    """
    Функция проверок ходов игроков
    :param current_player: 'крестик' или 'нолик'
    :param index: Размерность поля от 3 до 5
    :param field: Инициализированное поле с ходами игроков
    :return: Ход игрока для размещения на поле
    """
    while True:
        move = int(input(f'Чтобы поставить {current_player} укажите номер ячейки от 1 до {pow(index, 2)}:'))
        if move > pow(index, 2) or move < 0:
            print('Вы ввели неправильный номер ячейки')
            continue
        elif field[move - 1] == 'X' or field[move - 1] == '0':
            print('Ячейка занята!')
        else:
            break
    return move


def draw_field(field: List[str], index: int) -> None:
    """
    Функция отрисовки поля
    Поле фиксированного размера 3х3

    :param field: При начале игры - пустое поле, затем с ходами игроков
    :param index: Размерность поля от 3 до 5
    :return None: Печатает поле
    """
    field = [field[i:i + index] for i in range(0, index ** 2, index)]
    for row in field:
        for cell in row:
            print(f'|{cell:^3}', end='')
        print('|')


def who_win(field: List[str], index: int) -> int:
    """
    Функция проверки победы
    :param field: Поле после хода игрока
    :param index: Размерность поля
    :return win: 1(первый игрок выиграл), 2(второй) или 0(никто)
    """
    field_ = [field[i:i + index] for i in range(0, index ** 2, index)]
    field_trans = [[field_[j][i] for j in range(len(field_))] for i in range(len(field_[0]))]
    field_diagonal_first = [field[i] for i in range(0, index ** 2, index + 1)]
    field_diagonal_second = [field[i] for i in range(index - 1, ((index ** 2) - index + 1), index - 1)]
    win_field = field_ + field_trans
    win_field.append(field_diagonal_first)
    win_field.append(field_diagonal_second)
    win_comb = ['X'] * index
    win_comb_ = ['0'] * index
    for comb in win_field:
        if comb == win_comb:
            print('Выиграл игрок: 1')
            win = 1
            return win
        elif comb == win_comb_:
            print('Выиграл игрок: 2')
            win = 2
            return win
    win = 0
    return win


def game_continue(win: int) -> int:
    """
    Функция проверки окончания игры после каждого хода
    :param win: 1(первый игрок выиграл), 2(второй) или 0(никто)
    :return continue_: 0 - игра продолжается, 1 - игра окончена
    """
    if win == 0:
        continue_ = 0
        print(f'Игра продолжается: {continue_}')
        return continue_
    elif win != 0:
        continue_ = 1
        print(f'Игра окончена: {continue_}')
        return continue_


def player_step(field: List[str], move: int, current_player: str) -> List[str]:
    """
    Функция хода игроков
    :param field: Поле до хода игрока
    :param move: Введенный номер клетки игроком
    :param current_player: Крестик или нолик
    :return field: Новое поле после хода игрока
    """
    move_ = move - 1
    for value in field:
        if value == ' ':
            field[move_] = current_player
            return field


def start_game():
    """
    Функция определения размерности поля в пределах от 3 до 5
    :return index: Размерность поля
    """
    print('Договоритесь, кто играет "Х", а кто "0"')
    while True:
        try:
            index = int(input('Введите размерность поля от 2 до 5:'))
            if index < 2 or index > 5:
                print('Вы ввели неверное значение поля')
                continue
        except ValueError:
            print('Вам необходимо ввести число!')
            continue
        return index


def who_first() -> str:
    """
    Функция случайного определения, кто начинает игру
    :return: Крестик или нолик
    """
    list_ = ['X', '0']
    current_player = random.choice(list_)
    return current_player


def game() -> None:
    """
    Функция хода игры
    :return: None
    """
    index = start_game()
    field = [' '] * pow(index, 2)
    draw_field(field, index)
    current_player = who_first()
    count_step = 0
    print(f'Первым ходит "{current_player}"')
    while True:
        move = check_move(current_player, index, field)
        field = player_step(field, move, current_player)
        count_step += 1
        draw_field(field, index)
        win = who_win(field, index)
        continue_ = game_continue(win)
        if win != 0 or continue_ != 0:
            break
        elif count_step == pow(index, 2):
            print('Ничья!')
            break
        current_player = "X" if current_player == "0" else "0"


if __name__ == "__main__":
    game()
