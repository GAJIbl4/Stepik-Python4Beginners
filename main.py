import random


def input_number(low, large):  # Проверка введённых данных
    print('Введите целое число от ', low, ' до ', large, ': ', sep='')
    s = input()
    while not s.isdigit():
        s = input('А может быть все-таки введем целое число?\n')
    while int(s) > 100 or int(s) < 1:
        print('А может быть все-таки введем целое число от ', low, ' до ', large, ': ', sep='')
        s = input()
    return int(s)


def check(n, num):  # Проверка, угадал или нет
    if n < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif n > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        return True
    return False


def game(low, large):  # Процесс игры
    num = random.randint(low, large)  # Исходное число для угадывания
    count = 0  # Количество попыток
    flag_endgame = False  # Флаг конца игры

    while flag_endgame is False:
        n = input_number(low, large)
        if check(n, num):
            flag_endgame = True
        count += 1
    print('Общее количество попыток:', count)


def one_more():  # Проверка на повторную игру
    while True:
        s = input('Желаете сыграть ещё раз? (y/n) ')
        if s == 'y':
            return True
        elif s == 'n':
            return False


def game_range():
    low = 1
    large = 100
    while True:
        s = input('Не хотите выбрать диапазон угадывания чисел? (y/n) ')
        if s == 'y':
            break
        elif s == 'n':
            return low, large
    s = input('Введите нижний предел диапазона: ')
    while True:
        if s.isdigit():
            low = int(s)
            break
        else:
            s = input('Пожалуйста, введите целое число: ')
    s = input('Введите верхний предел диапазона: ')
    while True:
        if s.isdigit():
            large = int(s)
            break
        else:
            s = input('Пожалуйста, введите целое число: ')
    return low, large


flag_try_again = True
print('Добро пожаловать в числовую угадайку!')
print('Вы должны угадать число от 1 до 100')
while flag_try_again is True:
    a, b = game_range()
    game(a, b)
    flag_try_again = one_more()
print('Спасибо, что играли в числовую угадайку. Ещё увидимся!')

