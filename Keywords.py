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

print("Максимальное число из", a, "и", b, "это", x)


def empty_function():
    pass


def even_nums(n):
    i = 0
    for i in range(n):
        if i % 2 == 0:
            yield i


print(list(even_nums(n=int(input("Введите число n:")))))


def test_max_of_two_num():
    assert max_of_two_num(a, b) == x, "Ошибка: неправильное значение для различных пар"


test_max_of_two_num()
print("Все тесты пройдены!")
