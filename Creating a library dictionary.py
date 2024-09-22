library = {}

def add_book(title, author, year, availability):
    library[title] = {"author": author, "year": year, "availability": availability}

def display_books():
    for title, book_details in library.items():
        print(f"Название: {title}")
        print(f"Автор: {book_details['author']}")
        print(f"Год издания: {book_details['year']}")
        print(f"Наличие: {book_details['availability']}")
        print()