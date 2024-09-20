secret_password = 'ПАРОЛЬ'

attempts = 0
while True:
    attempts += 1
    password = input("Введите пароль: ")

    if password == secret_password:
        print(f"Пароль верен! Попыток: {attempts}")
        break
    elif attempts > 3:
        print("Достигнуто максимальное количество попыток входа! Доступ заблокирован.")
        break
    else:
        print(f"Неверный пароль. Попробуйте еще раз. Осталось {3 - attempts} попыток.")

print("Добро пожаловать!")
