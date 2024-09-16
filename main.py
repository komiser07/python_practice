num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Результат сложения: ", num1 + num2)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Результат вычитания: ", num1 - num2)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Результат умножения: ", num1 * num2)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
try:
    print("Результат деления: ", num1 / num2)
except ZeroDivisionError:
    print("Ошибка деления на ноль!")
