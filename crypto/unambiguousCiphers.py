r"""
Модуль реализующий шифрование/дешифрование текста по заданной последовательности символов и трём алгоритмам (Учитывая
символы нижнего\верхнего регистра и ",.\xa0" )
Алгоритмы: Атбаш, Цезарь, Квадрат Полибия
Студент: Королев Олег Александрович
"""


from crypto.base import Crypto
from crypto.base import Letters


class Atbash(Crypto):
    """ Шифр простой замены АТБАШ
    in:  а б в г д е ж з и й к л м н о п р с т у ф х ц ш щ ъ ы ь э ю я , .
    out: . , я ю э ь ы ъ щ ш ц х ф у т с р п о н м л к й и з ж е д г в б а
    """

    def __init__(self, message: str, letters: str = Letters.RU):
        super().__init__(message, letters)
        self.hint_title = 'Шифр простой замены АТБАШ'

    def encrypt(self=Crypto) -> str:
        """ Метод шифрования
        :return: зашифрованное сообщение
        """
        encrypted_message: str
        encrypted_chars = []
        for i, x in self.__get_char_sequence__():
            encrypted_char_number = len(self.letters) - i + 1
            y = self.__get_char_from_letters_number__(encrypted_char_number)
            encrypted_chars.append(y)

        encrypted_message = ''.join(encrypted_chars)
        return encrypted_message

    def decrypt(self) -> str:
        return self.encrypt()


class Cesar(Crypto):
    """ Шифр Цезаря
    in:  а б в г д е ж з и й к л м н о п р с т у ф х ц ш щ ъ ы ь э ю я , .
    out: г д е ж з и й к л м н о п р с т у ф х ц ш щ ъ ы ь э ю я а б в г д
    """

    def __init__(self, message: str, letters: str = Letters.RU):
        super().__init__(message, letters)

    def encrypt(self) -> str:
        encrypted_message: str
        encrypted_chars = []
        n = len(self.letters)
        for i, x in self.__get_char_sequence__():
            if i % n == i:
                y = self.__get_char_from_letters_number__(i + 3)
                encrypted_chars.append(y)

        encrypted_message = ''.join(encrypted_chars)
        return encrypted_message

    def decrypt(self) -> str:
        return self.encrypt()


class PolybiusSquare(Crypto):
    """ 3. Квадрат Полибия
    in:  Д  о  м     м  о  й  ,     к  а  к     б  ы     м  а  л     т  ы     н  и     б  ы  л  ,     т  ы     м ...
    out: 15,33,31,65,31,33,24,63,65,25,11,25,65,12,54,65,31,11,26,65,41,54,65,32,23,65,12,54,26,63,65,41,54,65,31...
    """

    def __init__(self, message: str, letters: str = Letters.RU):
        super().__init__(message, letters)
