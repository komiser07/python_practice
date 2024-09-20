def is_voter(age, citizenship, criminal_status):
    if age >= 18:
        print("Возраст соответствует требованиям.")
    else:
        print("Возраст не соответствует требованиям.")
        return False

    if citizenship == True:
        print("Вы являетесь гражданином.")
    else:
        print("Вы не являетесь гражданином.")
        return False

    if not criminal_status:
        print("У вас нет уголовного наказания.")
    else:
        print("У вас есть уголовное наказание.")
        return False

    return True


age = int(input("Введите ваш возраст: "))
citizenship = input("Являетесь ли вы гражданином? (Да/Нет) ")
criminal_status = input("Имеется ли у вас уголовное наказание? (Да/Нет) ")

if citizenship in ['Да', 'да']:
    citizen = True
else:
    citizen = False

if criminal_status in ['Нет', 'нет']:
    criminal = False
else:
    criminal = True

result = is_voter(age, citizen, criminal)

if result:
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать.")
