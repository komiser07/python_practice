def int_to_en(num):
    d = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }
    return d[num]


num = int(input("Введите число от 0 до 5:"))

print("Соответствющее слово: ", int_to_en(num))