def sum_of_even_numbers():
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
    return total


def odd_squares_list():
    squares = []
    for i in range(1, 11):
        if i % 2 != 0:
            squares.append((i * i))
    return squares


def count_user_inputs():
    count = 0
    while True:
        num = int(input("Введите целое число: "))
        if num < 0:
            break
        else:
            count += 1
    print("Количество введенных положительных чисел:", count)


count_user_inputs()

print("Сумма всех четных чисел от 1 до 100 равна", sum_of_even_numbers())
print("Список квадратов нечетных чисел от 1 до 10:", odd_squares_list())