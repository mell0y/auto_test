# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_first():
    assert all_division(12, 2) == 6


def test_large():
    assert all_division(1000000, 100000) == 10


def test_float():
    assert all_division(10, 0.5) == 20


def test_negative():
    assert all_division(-3, -1) == 3


def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(22, 0)
