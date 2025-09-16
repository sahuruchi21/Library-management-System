import os

DATA_DIR = "data"
BOOKS_FILE = os.path.join(DATA_DIR, "books.txt")
USERS_FILE = os.path.join(DATA_DIR, "users.txt")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def add_book(book_name):
    with open(BOOKS_FILE, "a") as f:
        f.write(book_name + "\n")
    return f"Book added: {book_name}"

def view_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r") as f:
        return [line.strip() for line in f]

def search_book(book_name):
    books = view_books()
    return book_name in books

def issue_book(book_name, user_name):
    if search_book(book_name):
        with open(USERS_FILE, "a") as f:
            f.write(f"{user_name} issued {book_name}\n")
        return True
    return False

def view_issued_books():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return [line.strip() for line in f]
