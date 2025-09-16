# 📚 Library Management System (C++)

A simple **Library Management System (LMS)** built in **C++**, designed with modular structure and basic file handling.  
Includes **unit tests using Google Test (gtest)** to ensure reliability of core functions.

---

## 🚀 Features
- ➕ Add new books to the library  
- 📖 View available books  
- 🔍 Search for a book by title  
- 📝 Issue a book to a user  
- 📋 View all issued books  

---

## 🛠️ Tech Stack
- **Language**: C++  
- **Unit Testing**: Google Test (gtest)  
- **Build Tools**: MinGW / MSVC / g++ (any C++17+ compiler)  

---

## 📂 Project Structure
Library-Management-System/
│
├── backend/
│ ├── lms.cpp # Implementation of core LMS functions
│ ├── lms.h # Header file
│
├── tests/
│ └── test.cpp # Unit tests using gtest
│
├── README.md # Documentation
└── .gitignore # Ignore build files

yaml
Copy code

---

## ⚡ Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Library-Management-System.git
cd Library-Management-System
2️⃣ Compile the project
bash
Copy code
g++ backend/lms.cpp -o lms
./lms
3️⃣ Run Unit Tests (Google Test)
Make sure you have gtest installed. Then:

bash
Copy code
g++ tests/test.cpp backend/lms.cpp -lgtest -lgtest_main -pthread -o test
./test
✅ Example Unit Test
cpp
Copy code
#include "lms.h"
#include <gtest/gtest.h>

TEST(LibraryTest, AddBook) {
    Library lib;
    EXPECT_TRUE(lib.addBook("C++ Basics"));
    EXPECT_TRUE(lib.searchBook("C++ Basics"));
}
