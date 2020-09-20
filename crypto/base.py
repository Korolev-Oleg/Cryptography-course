from string import ascii_letters
from abc import ABCMeta, abstractmethod, ABC
from dataclasses import dataclass

POSTFIX_LETTERS = ',.\x20'
RU_LETTERS = 'абвгдежзийклмнопрстуфхцшщъыьэюя'


@dataclass
class Letters:
    RU = f'{RU_LETTERS}{RU_LETTERS.upper()}{POSTFIX_LETTERS}'
    EN = f'{ascii_letters}{POSTFIX_LETTERS}'
    current: str


class Crypto(object):
    """ Базовый класс, описывающий сущность шифрования """
    __metaclass__ = ABCMeta
    letters = str
    message: str
    hint_title: str

    def __init__(self, message: str, letters: str):
        self.letters = letters
        self.message = message
        self.__check_letters__()

    @abstractmethod
    def encrypt(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def decrypt(self) -> str:
        raise NotImplementedError()

    def get_hint(self) -> str:
        """ Формирует подсказку на примере алфавита """
        old_message, self.message = self.message, self.letters
        hint = f"{self.hint_title}:\n{self.letters}\n{self.encrypt()}"
        self.message = old_message
        return hint

    def __check_letters__(self):
        """ Проверяет соответствие сообщения выбранному алфавиту """
        for char in self.message:
            if char not in self.letters:
                print(char, 'not in ', self.letters)
                raise SyntaxError(f'The message does not match the selected letters ({self.letters})')

    def __get_char_sequence__(self) -> tuple:
        """ Генератор последовательность номеров букв сообщения в открытом алфавите
        :rtype: tuple (int: Номер буквы сообщения в открытом алфавите, str: буква сообщения)
        """
        for find_char in self.message:
            for i, char in enumerate(self.letters):
                if char == find_char:
                    yield i + 1, char

    def __get_char_from_letters_number__(self, i: int) -> str:
        return self.letters[i - 1]