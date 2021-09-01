def rot(char, sh, lang):  # Операция сдвига на num символов
    if char.isupper():
        if lang == 'eng':
            if ord(char) + sh > 90:
                return chr(ord(char) + sh - 26)
            else:
                return chr(ord(char) + sh)
        elif lang == 'ru':
            if ord(char) + sh > 1071:
                return chr(ord(char) + sh - 32)
            else:
                return chr(ord(char) + sh)
    elif char.islower():
        if lang == 'eng':
            if ord(char) + sh > 122:
                return chr(ord(char) + sh - 26)
            else:
                return chr(ord(char) + sh)
        elif lang == 'ru':
            if ord(char) + sh > 1103:
                return chr(ord(char) + sh - 32)
            else:
                return chr(ord(char) + sh)
    return chr(ord(char) + sh)


def data_in():  # Запрос начальных данных
    while True:
        lang = input('Для начала шифрования укажите желаемый язык алфавита(ru/eng):\n')
        if lang == 'ru' or lang == 'eng':
            break
    while True:
        sh = input('Выберите шаг сдвига вправо(1 - ∞):\n')
        if sh.isdigit():
            if int(sh) > 0:
                break
            else:
                print('Шаг сдвига должен быть натуральным числом!')
        else:
            print('Шаг сдвига должен быть натуральным числом!')
    da = input('Введите информацию, которую желаете зашифровать:\n')
    return lang, int(sh), da


def crypt(lang, sh, da):
    answer = ''
    if lang == 'ru':
        while sh > 32:
            sh -= 32
    elif lang == 'eng':
        while sh > 26:
            sh -= 26
    for i in range(len(da)):
        if da[i].isalpha():
            answer += rot(da[i], sh, lang)
        else:
            answer += da[i]
    return answer


print('Вас приветствует шифровщик Цезаря')
flag = True
while flag is True:
    language, shift, data = data_in()
    print(crypt(language, shift, data))
    while True:
        s = input('Желаете зашифровать ещё что-нибудь? (y/n)\n')
        if s == 'y':
            break
        elif s == 'n':
            flag = False
            break
print("Обращайтесь, если нужно будет что-нибудь зашифровать!")
