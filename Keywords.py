def max_of_two_num(a, b):
    if a > b:
        return a

    elif a == b:
        print("a равно b")

    else:
        return b


a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))

x = max_of_two_num(a, b)


def empty_function():
    pass


def even_nums(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


def test_max_of_two_num():
    assert max_of_two_num(57, 34) == 57, "Ошибка: неправильное значение для различных пар"
    assert max_of_two_num(-1, 1) == 1, "Ошибка: неправильное значение для различных пар"
    assert max_of_two_num(65, 64) == 65, "Ошибка: неправильное значение для различных пар"


test_max_of_two_num()

print("Максимальное число из", a, "и", b, "это", x)
print(list(even_nums(int(input("Введите число n:")))))
print("Все тесты пройдены!")
