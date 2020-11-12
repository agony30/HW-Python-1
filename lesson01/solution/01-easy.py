# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
number = input("Type number: ")

# 01-1
a = int(number)

while a > 0:
    current, a = a % 10, a // 10
    print(current)

# 01-2
for x in number:
    print(x)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# 02-1
a = int(input("First number: "))
b = int(input("Second number: "))

c = a
a = b
b = c

print(a, b)

# 02-2
a = int(input("First number: "))
b = int(input("Second number: "))

a = a + b
b = a - b
a = a - b

print(a, b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# 03-1
age = int(input("Your age: "))

if age < 18:
    print("Sorry")
else:
    print("Success")