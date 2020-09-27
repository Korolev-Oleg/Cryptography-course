from abc import ABCMeta, abstractmethod, ABC
from string import ascii_letters
from string import digits

POSTFIX_LETTERS = ',.\x20'
RU_LETTERS = 'абвгдежзийклмнопрстуфхцшщъыьэюя'


class Letters:
    RU = RU_LETTERS + RU_LETTERS.upper() + POSTFIX_LETTERS
    EN = ascii_letters + POSTFIX_LETTERS
    DIGITS = digits
    current: str


class BaseCrypto(object):
    """ Базовый класс, описывающий сущность шифрования """
    __metaclass__ = ABCMeta
    letters = Letters.RU
    message: str

    def __init__(self, message: str, letters=None):
        self.message = message
        if letters:
            try:
                self.letters = letters
                self._check_letters()
            except SyntaxError:
                self.letters = letters + Letters.DIGITS
                self._check_letters()
        else:
            self.__set_letters__()

    @abstractmethod
    def encrypt(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def decrypt(self) -> str:
        raise NotImplementedError()

    def get_hint(self) -> str:
        """ Формирует подсказку на примере алфавита """
        old_message = self.message
        self.message = self.letters
        hint = f"\n{self.letters}\n{self.encrypt()}"
        self.message = old_message
        return hint

    def __set_letters__(self):
        """ Выбирает язык символов алфавита En/Ru """

        # Перебор алфавитов
        def roll_letters(with_digits=False):
            for i, key in enumerate(Letters.__dict__):
                if i < len(Letters.__dict__):
                    if not key.startswith('__'):
                        self.letters = Letters.__dict__[key] + Letters.DIGITS if with_digits else ''
                        if not self.__is_letters_error__():
                            break

            if not with_digits:
                roll_letters(with_digits=True)

            self._check_letters()
        roll_letters()

    def _check_letters(self):
        is_error = self.__is_letters_error__()
        if is_error:
            raise SyntaxError(f'Символ "{is_error}" не найден в выбранном алфавите: "{self.letters}"')

    def __is_letters_error__(self):
        """ Проверяет соответствие сообщения выбранному алфавиту """
        for char in self.message:
            if char not in self.letters:
                return char

        return False

    def _ord(self, char: str) -> int:
        return list(self.letters).index(char)

    def _chr(self, index: int) -> str:
        return list(self.letters)[index]


if __name__ == '__main__':
    s = BaseCrypto('test руский')
    print(s.letters)
