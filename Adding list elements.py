first_list = list(map(int, input("Введите первый список через пробел: ").split()))
second_list = list(map(int, input("Введите второй список через пробел: ").split()))

if len(first_list) != len(second_list):
    print("Списки должны иметь одинаковую длину.")
    exit()
else:
    new_list = []
    for i in range(len(first_list)):
        new_list.append(first_list[i] + second_list[i])

    print("Результат: ", end="")
    for num in new_list:
            print(num, end=" ")
