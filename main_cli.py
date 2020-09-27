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
    1) Авто
    2) Свой
    3) {Letters.RU}
    4) {Letters.EN}
    5) Выход""")

    choice = int(input(': '))
    if choice == 1:
        letters = None
    elif choice == 2:
        letters = input('Введите свой вариант алфавита:\n')
    elif choice == 3:
        letters = Letters.RU
    elif choice == 4:
        letters = Letters.EN
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


def pause(msg=None):
    input(msg if msg else 'Enter для продолжения...')
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    while True:
        message = str(input(f"Введите сообщение: ")).replace('\n', '').strip()
        letters = __choice_letters__()
        try:
            cipher = __choice_of_cipher__(message, letters)
            print(cipher.get_hint(), end='\n\n')
            print('X =', message)
            print('Y =', cipher.encrypt())
            pause()
        except SyntaxError as error:
            pause(error)
