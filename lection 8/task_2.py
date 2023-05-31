# Напишите класс Trigon, для инициализации передаётся неизвестное кол-во атрибутов

# В классе при инициализации происходит проверка на корректность переданных данных и генерируются следующие исключения:

# 1) Если хотя бы одна сторона передана не числом,
# то падаем с TypeError и текстом 'Стороны должны быть числами'

# 2) Если хотя бы одна сторона передана нулем или отрицательным числом,
# то падаем с ValueError и текстом 'Стороны должны быть положительными'

# 3) Если не соблюдается неравество треугольника,
# то Exception и текст "Не треугольник"

# 4) Если передано не 3 аргумента, то IndexError "Передано {n} аргументов, а ожидается 3", где n - кол-во аргументов

import unittest  # Не удалять


class Trigon:
    """
    Класс обрабатывает неизвестное кол-во атрибутов на вход и проверяет соблюдены ли все
     требования на соответствие треугольнику.
    """
    def __init__(self, *num):
        """
        :param num: Все полученные данные на вход передаются в переменную.
        """
        self.num = num

    @property
    def triangle(self):
        """
        Функция проверяет корректность полученных данных на соответствие треугольнику, если возникает исключение
        то, обрабатывает его и возвращает описание исключения.
        :return: Возвращаем возникшее исключение.
        """
        if len(self.num) != 3:
            raise IndexError(f"Передано {len(self.num)} аргументов, а ожидается 3")
        try:
            self.num[0] + self.num[1] + self.num[2]
        except TypeError:
            return 'Стороны должны быть числами'
        try:
            self.num[0] <= 0 or self.num[1] <= 0 or self.num[2] <= 0
        except ValueError:
            return 'Стороны должны быть положительными'
        if not (self.num[0] == self.num[1] == self.num[3]
                or self.num[0] == self.num[1] != self.num[3] or self.num[0] == self.num[3] != self.num[1]
                or self.num[1] == self.num[3] != self.num[0]):
            return "Не треугольник"


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, '7', 5), (-3, 7, 5), (2, 5, 2), (3, 4, 5, 6), (3, 4), (3, 4, 5)]

        test_data = [('Стороны должны быть числами', 'TypeError'),
                     ('Стороны должны быть положительными', 'ValueError'),
                     ("Не треугольник", 'Exception'),
                     ("Передано 4 аргументов, а ожидается 3", 'IndexError'),
                     ("Передано 2 аргументов, а ожидается 3", 'IndexError'),
                     0]
        for i, d in enumerate(data):
            try:
                Trigon(*data[i])
            except Exception as e:
                assert e.args[0] == test_data[i][0], 'Исключение имеет неправильный текст'
                assert type(e).__name__ == test_data[i][1], 'У исключения неправильный тип'

        print('Всё ок')


if __name__ == '__main__':
    unittest.main()
