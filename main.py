num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Результат сложения: ", num1 + num2)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Результат вычитания: ", num1 - num2)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Результат умножения: ", num1 * num2)

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print("Результат деления: ", num1 / num2)
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка деления на ноль!")
finally:
    print("Завершение работы программы.")
