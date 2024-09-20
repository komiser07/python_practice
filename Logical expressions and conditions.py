def is_voter(age, citizenship, criminal_status):
    return age >= 18 and citizenship and not criminal_status

def enter_data():
    age = int(input("Введите ваш возраст: "))
    citizenship = input("Являетесь ли вы гражданином? (Да/Нет) ").lower() == "да"
    criminal_status = input("Имеется ли у вас уголовное наказание? (Да/Нет) ").lower() == "да"
    output_result(age, citizenship, criminal_status)

def output_result(age, citizenship, criminal_status):
    if is_voter(age, citizenship, criminal_status):
        print("Вы можете голосовать!")
    else:
        print("Вы не можете голосовать.")

enter_data()

