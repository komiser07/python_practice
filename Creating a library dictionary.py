library = {}

def display_books():
    for title, book_details in library.items():
        print(f"title: {title}")
        print(f"author: {book_details['author']}")
        print(f"year: {book_details['year']}")
        print(f"availability: {book_details['availability']}")
        print()
