from abc import ABCMeta, abstractmethod, ABC
from string import ascii_letters
from string import digits

SPACE = ',.\x20'
RU_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


class Letters:
    RU = RU_LETTERS + RU_LETTERS.upper() + SPACE
    EN = ascii_letters + SPACE
    SYMBOLS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' + digits
    current: str


class BaseCrypto(object):
    """ Базовый класс, описывающий сущность шифрования """
    __metaclass__ = ABCMeta
    letters = Letters.RU
    message: str

    def __init__(self, message: str, letters=None):
        self.message = message
        if letters:
            self.letters = letters
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
        hint = f"{self.letters}\n{self.encrypt()}"
        self.message = old_message
        return hint

    def __set_letters__(self):
        """ Выбирает язык символов алфавита En/Ru """

        # Перебор алфавитов
        def roll_letters(self, with_symbols=False):
            for i, key in enumerate(Letters.__dict__):
                if i < len(Letters.__dict__):
                    if not key.startswith('__'):
                        letters = Letters.__dict__[key]
                        self.letters = letters + Letters.SYMBOLS if with_symbols else letters
                        if not self.__is_letters_error__():
                            return

            if not with_symbols:
                roll_letters(self, with_symbols=True)

            self._check_letters()

        roll_letters(self)

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

    def test(self):
        message = self.message
        encrypted = self.encrypt()
        self.message = encrypted
        decrypted = self.decrypt()

        return f"message:\t{message}\nencrypted:\t{encrypted}\ndecrypted:\t{decrypted}\nhint:\n{self.get_hint()}"


if __name__ == '__main__':
    s = BaseCrypto('test руский')
    print(s.letters)
