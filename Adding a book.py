library = {}


def add_book(title, author, year):
    global library

    if title in library:
        print(f"Книга '{title}' уже существует. Обновляем информацию.")
        book_details = library[title]
        book_details["author"] = author
        book_details["year"] = year
        book_details["availability"] = None
    else:
        library[title] = {"author": author, "year": year, "availability": None}
        print(f"Книга '{title}' успешно добавлена.")


def display_books():
    for title, book_details in library.items():
        print(f"Title: {title}")
        print(f"Author: {book_details['author']}")
        print(f"Year of publication: {book_details['year']}")
        print(f"Availability: {book_details['availability']}")
        print()


add_book("Путешествия Гулливера", "Джонатан Свифт", 1726)
add_book("Робинзон Крузо", "Даниэль Дефо", 1719)
add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
add_book("Думай и богатей", "Наполеон Хилл", 1937)

display_books()
