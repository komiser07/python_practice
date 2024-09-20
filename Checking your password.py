secret_password = 'ПАРОЛЬ'
while True:
    password = input("Введите пароль: ")

    if password == secret_password:
        print(f"Пароль верен!")
    else:
        print(f"Неверный пароль. Попробуйте еще раз.")

print("Добро пожаловать!")
