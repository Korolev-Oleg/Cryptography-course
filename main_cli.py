import os

from crypto.base import Letters
from crypto.unambiguousCiphers import (
    Atbash,
    Cesar,
    PolybiusSquare)


def __choice_letters__():
    """ Выбор алфавита в консоле """
    global letters
    print(f"""Выбирите вариант алфавита:
    1) {Letters.RU}
    2) {Letters.EN}
    3) Свой
    4) Выход""")

    choice = int(input(': '))
    if choice == 1:
        letters = Letters.RU
    elif choice == 2:
        letters = Letters.EN
    elif choice == 3:
        letters = input('Введите свой вариант алфавита:\n')
    else:
        exit()

    return letters


def __choice_of_cipher__(m, l):
    """ выбор шифшра в консоле """
    print(f"""Выбирите шифр:
    1) Шифр АТБАШ,.
    2) Шифр Цезаря
    3) Квадрат Полибия
    """)

    choice = int(input(': '))
    if choice == 1:
        chosen_cipher = Atbash(message=m, letters=l)
    elif choice == 2:
        chosen_cipher = Cesar(message)
    else:
        chosen_cipher = PolybiusSquare(message)

    return chosen_cipher


if __name__ == '__main__':
    while True:
        message = str(input(f"Введите сообщение: ")).replace('\n', '').strip()
        letters = __choice_letters__()
        try:
            cipher = __choice_of_cipher__(message, letters)
            print('X =', message)
            print('Y =', cipher.encrypt())
            print(cipher.get_hint(), end='\n\n')
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        except SyntaxError as error:
            print(error, end='\n\n')
