r"""
Модуль реализующий шифрование/дешифрование текста по заданной последовательности символов и трём алгоритмам (Учитывая
символы нижнего\верхнего регистра и ",.\xa0" )
Алгоритмы: Атбаш, Цезарь, Квадрат Полибия
Студент: Королев Олег Александрович
"""
from typing import Tuple, Any

from crypto.base import BaseCrypto
from crypto.base import Letters


class Atbash(BaseCrypto):
    """ Шифр простой замены АТБАШ
    in:  а б в г д е ж з и й к л м н о п р с т у ф х ц ш щ ъ ы ь э ю я , .
    out: . , я ю э ь ы ъ щ ш ц х ф у т с р п о н м л к й и з ж е д г в б а
    """

    def encrypt(self) -> str:
        """ Метод шифрования
        :return: зашифрованное сообщение
        """

        def get_shift(char):
            return self._chr(len(self.letters) - self._ord(char) - 1)

        return ''.join([get_shift(char) for char in self.message])

    def decrypt(self) -> str:
        return self.encrypt()


class Cesar(BaseCrypto):
    """ Шифр Цезаря
    in:  а б в г д е ж з и й к л м н о п р с т у ф х ц ш щ ъ ы ь э ю я , .
    out: г д е ж з и й к л м н о п р с т у ф х ц ш щ ъ ы ь э ю я а б в г д
    """

    def encrypt(self, shift=3) -> str:
        def get_shift(char):
            return self._chr((self._ord(char) + shift) % len(self.letters))

        return ''.join([get_shift(char) for char in self.message])

    def decrypt(self, shift=3) -> str:
        return self.encrypt(shift=-shift)


class PolybiusSquare(BaseCrypto):
    """ 3. Квадрат Полибия
    in:  Д  о  м     м  о  й  ,     к  а  к     б  ы     м  а  л     т  ы     н  и     б  ы  л  ,     т  ы     м ...
    out: 15,33,31,65,31,33,24,63,65,25,11,25,65,12,54,65,31,11,26,65,41,54,65,32,23,65,12,54,26,63,65,41,54,65,31...
    """
    square = []
    cut: int

    def render_square(self):
        cut = 0
        while pow(cut, 2) < len(self.letters):
            cut += 1

        square = []
        string_length = (int(len(self.letters) / cut))
        for string_num in range(string_length):
            if string_num > 0:
                square.append(self.letters[cut * string_num:cut * (string_num + 1)])
            else:
                square.append(self.letters[:cut])

        self.cut = cut
        self.square = square

    def ord(self, char: str) -> Tuple[int, int]:
        if not self.square:
            self.render_square()

        for str_num, string in enumerate(self.square):
            if char in string:
                return str_num, string.index(char)

    def chr(self, row: int, col: int) -> str:
        if not self.square:
            self.render_square()

        return self.square[row][col]

    def encrypt(self, list_result=False) -> Any:

        keys = []
        for char in self.message:
            keys.append(self.ord(char))

        if list_result:
            encrypted_message = keys
        else:
            encrypted_message = ' '.join([f'{row}{col}' for row, col in keys])

        return encrypted_message

    def decrypt(self, sep=' ') -> str:
        if isinstance(self.message, str):
            keys_list = self.message.split(sep)
        else:
            keys_list = self.message

        return ''.join([self.chr(row=int(row), col=int(col)) for row, col in keys_list])


if __name__ == '__main__':
    crypto = PolybiusSquare('21 04 20 21 60 13 04 20 20 00 06 04', letters=Letters.EN)
    print(crypto.decrypt())
