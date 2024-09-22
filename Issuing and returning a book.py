library = {}


def add_book(title, author, year):
    if title in library:
        choice = input("Книга '" + title + "' уже существует. Обновить информацию? (Y/N): ")
        if choice.upper() == 'Y':
            book_details = library[title]
            library[title] = {"author": author, "year": year, "availability": book_details["availability"]}
            print(f"Информация о книге '{title}' обновлена.")
        else:
            print("Отменено обновление.")
    else:
        library[title] = {"author": author, "year": year, "availability": None}
        print(f"Книга '{title}' успешно добавлена.")


def issue_book(title):
    if title in library:
        book_details = library[title]
        book_details["availability"] = "выдана"
        print(f"Книга '{title}' успешно выдана.\n")
    else:
        print(f"Книга '{title}' не найдена.")


def return_book(title):
    if title in library:
        book_details = library[title]
        book_details["availability"] = "в наличии"
        print(f"Книга '{title}' успешно возвращена.\n")
    else:
        print(f"Книга '{title}' не найдена.")


def remove_book(title):
    if title in library:
        del library[title]
        print(f"Книга '{title}' успешно удалена.\n")
    else:
        print(f"Книга '{title}' не найдена.\n")


def display_books():
    for title, book_details in library.items():
        print(f"Title: {title}")
        print(f"Author: {book_details['author']}")
        print(f"Year of publication: {book_details['year']}")
        print(f"Availability: {book_details['availability']}\n")


add_book("Путешествия Гулливера", "Джонатан Свифт", 1726)
add_book("Робинзон Крузо", "Даниэль Дефо", 1719)
add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
add_book("Думай и богатей", "Наполеон Хилл", 1937)

display_books()

issue_book("Путешествия Гулливера")
display_books()

return_book("Путешествия Гулливера")
display_books()
