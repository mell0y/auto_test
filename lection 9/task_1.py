# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


original_file = open("test_file/task1_data.txt", encoding='utf-8')
result = open("test_file/task1_answer.txt", mode='w', encoding='utf-8')


def del_int():
    """
    Функция открывает txt файл по заданному пути и убирает все цифры из файла.
    :return: Возвращаем строку без цифр
    """
    no_numbers = []
    for i in original_file:
        for letter in i:
            if not letter.isdigit():
                no_numbers.append(letter)
    return "".join(no_numbers)


result.write(del_int())
original_file.close()
result.close()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
