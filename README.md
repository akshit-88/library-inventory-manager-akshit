📚 Library Inventory Manager

A Mini Project for Programming for Problem Solving using Python

👨‍💻 Author

Akshit
Roll No: 2501730020
Course: B.Tech CSE (AI & ML)
Section: E

📝 Project Overview

The Library Inventory Manager is a simple command-line application designed to help a library track and manage books.
It uses:

Object-Oriented Programming (OOP)

JSON file handling

Exception handling

Python logging

Modular project structure

This project allows adding, issuing, returning, searching, and viewing books.
All data is stored persistently in a JSON file (catalog.json).

🎯 Features
✔ 1. Book Management

Add a new book

Issue a book (mark as issued)

Return a book (mark as available)

Check availability

✔ 2. Search

Search books by title

Search books by ISBN

✔ 3. View Inventory

Display all books with details

Automatic data saving to JSON

✔ 4. Robust File Handling

Handles missing JSON files

Repairs corrupted JSON

Loads catalog automatically

✔ 5. Logging

All major actions logged (INFO, ERROR)

✔ 6. Correct OOP Structure

Book class

LibraryInventory class

CLI menu interface

📂 Project Structure

library-inventory-manager-akshit/

│
 ├── catalog.json

├── library_manager/ 

   ├── __init__.py
│   ├── book.py
│   └── inventory.py
    └── logger_config.py

├── cli/
│   └── main.py

├── README.md