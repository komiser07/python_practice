with open('data.txt', 'w') as file:
    file.write("Доброе утро\n")
    file.write("Добрый день\n")
    file.write("Добрый вечер\n")

with open('data.txt', 'r') as file:
    print(file.read())

with open('data.txt', 'a') as file:
    file.write("Доброй ночи\n")
    file.write("Пора вставать\n")

with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

with open('data.txt', 'rb') as source:
    with open('copy_of_data.txt', 'wb') as copy_file:
        copy_file.write(source.read())