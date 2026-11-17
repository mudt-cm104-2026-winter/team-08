"""Where the books are kept.

A Python list in memory. Simple, and it forgets everything when the app
restarts. That is fine for this stage.

Every book is a dictionary with an id, a title, an author and a status.
The status says in which column the book is:
"want" (want to read), "reading" (currently reading) or "finished".
"""

_books = []
_next_id = 1


def books_with_status(status):
    """All books of one column, sorted A-Z by title."""
    found = [book for book in _books if book["status"] == status]
    return sorted(found, key=lambda book: book["title"].lower())


def add_book(title, author):
    """Store a new book. It starts in the "want to read" column."""
    global _next_id
    book = {"id": _next_id, "title": title, "author": author, "status": "want"}
    _books.append(book)
    _next_id += 1


def move_book(book_id, status):
    """Put a book into another column."""
    for book in _books:
        if book["id"] == book_id:
            book["status"] = status


def delete_book(book_id):
    """Remove a book from the list."""
    for book in _books:
        if book["id"] == book_id:
            _books.remove(book)
            return
