import streamlit as st
import sys
import os
import pandas as pd

# --- Fix Python import path for backend ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.lms import add_book, view_books, search_book, issue_book, view_issued_books

# Streamlit page config
st.set_page_config(page_title="Library Management System", layout="wide")
st.title("📚 Library Management System")

# Sidebar menu
menu = ["Add Book", "View Books", "Search Book", "Issue Book", "View Issued Books"]
choice = st.sidebar.selectbox("Menu", menu)

# --- ADD BOOK ---
if choice == "Add Book":
    book_name = st.text_input("Book Name")
    if st.button("Add"):
        if book_name.strip() != "":
            msg = add_book(book_name.strip())
            st.success(msg)
        else:
            st.warning("Please enter a valid book name.")

# --- VIEW BOOKS ---
elif choice == "View Books":
    books = view_books()
    if books:
        st.table(pd.DataFrame(books, columns=["Books"]))
    else:
        st.info("No books available.")

# --- SEARCH BOOK ---
elif choice == "Search Book":
    book_name = st.text_input("Enter Book Name to Search")
    if st.button("Search"):
        if book_name.strip() != "":
            if search_book(book_name.strip()):
                st.success(f"{book_name.strip()} is available!")
            else:
                st.error(f"{book_name.strip()} not found.")
        else:
            st.warning("Please enter a valid book name.")

# --- ISSUE BOOK ---
elif choice == "Issue Book":
    book_name = st.text_input("Book Name")
    user_name = st.text_input("User Name")
    if st.button("Issue"):
        if book_name.strip() == "" or user_name.strip() == "":
            st.warning("Please enter both book name and user name.")
        else:
            if issue_book(book_name.strip(), user_name.strip()):
                st.success(f"{book_name.strip()} issued to {user_name.strip()}")
            else:
                st.error(f"{book_name.strip()} is not available.")

# --- VIEW ISSUED BOOKS ---
elif choice == "View Issued Books":
    issued = view_issued_books()
    if issued:
        st.table(pd.DataFrame(issued, columns=["Issued Records"]))
    else:
        st.info("No books have been issued yet.")
