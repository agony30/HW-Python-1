# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

# Раз, Два, Три

list_1 = ["яблоко", "банан", "киви", "арбуз", "авокадододо"]
a = 0
for i in list_1:
    if len(i) > a:
        a = len(i)
for i in list_1:
    print("{:>{}}".format(i, a))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_3 = [10, 20, 30, 40, 70, 80]
list_2 = [30, 40, 5, 6, 9]

list_3 = list(set(list_3).difference(list_2))

print(list_3)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_4 = [1, 10, 3, 4, 5, 6, 7, 8, 11, 13, 20]
j = 0
for i in list_4:
    if i % 2 == 0:
        list_4[j] = (i / 4)
        j += 1
    else:
        list_4[j] = (i * 2)
        j += 1

print(list_4)
