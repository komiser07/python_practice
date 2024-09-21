def calculate_average(grades):
    return sum(grades) / len(grades)


def student_is_successful(student, threshold=75):
    if student['average'] >= threshold:
        return 'успешен'
    else:
        return 'отстающий'


def format_student_info(student):
    average = round(student['average'], 2)
    success = student_is_successful(student)
    return f"Студент: {student['name']}\nСредний балл: {average}\nСтатус: {success}\n"


def main():
    students = [
        {'name': 'Святозар', 'grades': [80, 90, 75, 95]},
        {'name': 'Марфа', 'grades': [90, 85, 70, 80, 95]},
        {'name': 'Елисей', 'grades': [60, 20, 80, 90, 85]},
        {'name': 'Добрыня', 'grades': [60, 70, 80, 90, 85]}
    ]

    overall_average = 0

    for student in students:
        grades = student['grades']
        student['average'] = calculate_average(grades)
        overall_average += student['average']
        print(format_student_info(student))

    overall_average /= len(students)
    print(f"Общий средний балл: {overall_average:}")

    new_student = {'name': 'Коловрат', 'grades': [80, 75, 90, 85]}
    new_student['average'] = calculate_average(new_student['grades'])
    students.append(new_student)

    min_student = min(students, key=lambda s: s['average'])
    students.remove(min_student)

    print("\n\nНовые данные после добавления и удаления:")
    for student in students:
        print(format_student_info(student))


main()
