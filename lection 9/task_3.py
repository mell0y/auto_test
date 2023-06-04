# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open("test_file/task_3.txt") as file:
    total_prices = []
    purchase = []
    for i in file:
        if i.strip():
            purchase.append(int(i.strip()))
        else:
            if purchase:
                total_prices.append(sum(purchase))
                purchase = []
    three_most_expensive_purchases = sum(sorted(total_prices)[-3:])

assert three_most_expensive_purchases == 202346
print('Все ок')
