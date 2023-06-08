# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_word_1 = ''
    random_word_2 = ''
    while True:
        for i in range(random.randint(1, 15)):
            random_word_1 += random.choice(letters)
        for i in range(random.randint(1, 15)):
            random_word_2 += random.choice(letters)
        yield random_word_1 + ' ' + random_word_2
        random_word_1 = ''
        random_word_2 = ''


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
