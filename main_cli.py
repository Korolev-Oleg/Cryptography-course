import os

from crypto.base import Letters
from crypto.unambiguousCiphers import (
    Atbash,
    Cesar,
    PolybiusSquare)


def clear():
    os.system('clear' if not os.name == 'nt' else 'cls')


def pause(msg=None):
    input(msg if msg else 'Enter для продолжения...')


def choice_letters():
    """ Выбор алфавита в консоле """
    global letters
    clear()
    print(f"""Выбирите вариант алфавита:
    1) Авто
    2) Свой
    3) {Letters.RU}
    4) {Letters.EN}
    5) {Letters.SYMBOLS}
    6) Выход""")

    choice = int(input(': '))
    if choice == 1:
        letters = None
    elif choice == 2:
        letters = input('Введите свой вариант алфавита:\n')
    elif choice == 3:
        letters = Letters.RU
    elif choice == 4:
        letters = Letters.EN
    elif choice == 5:
        letters = Letters.SYMBOLS
    else:
        exit()

    return letters


def choice_of_cipher(m, l):
    """ выбор шифшра в консоле """
    clear()
    print(f"""Выбирите шифр:
    1) Шифр АТБАШ,.
    2) Шифр Цезаря
    3) Квадрат Полибия""")

    choice = int(input(': '))
    if choice == 1:
        chosen_cipher = Atbash(message=m, letters=l)
    elif choice == 2:
        chosen_cipher = Cesar(message=m, letters=l)
    else:
        chosen_cipher = PolybiusSquare(message=m, letters=l)

    return chosen_cipher


def choice_method(cipher):
    clear()
    print(f"""Выбирите метод:
    1) Зашифровать
    2) Расшифровать
    """)
    chose = int(input())
    if chose == 1:
        return lambda: cipher.encrypt()
    else:
        return lambda: cipher.decrypt()


if __name__ == '__main__':
    while True:
        clear()
        message = str(input(f"Введите сообщение: ")).replace('\n', '').strip()
        letters = choice_letters()
        try:
            cipher = choice_of_cipher(message, letters)
            cipher_method = choice_method(cipher)
            clear()
            print('Подсказка шифра:')
            print(cipher.get_hint(), '\n\n', 'Результат:')
            print('X =', message)
            print('Y =', cipher_method(), '\n')
            pause()
        except Exception as error:
            pause(error)
