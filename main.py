from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    print("\n----- Library Menu -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def run():
    lib = LibraryInventory()

    while True:
        menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                t = input("Title: ")
                a = input("Author: ")
                i = input("ISBN: ")
                lib.add_book(Book(t, a, i))
                print("Book added successfully!")

            elif choice == "2":
                isbn = input("Enter ISBN: ")
                book = lib.search_by_isbn(isbn)
                if book and book.issue():
                    lib.save_data()
                    print("Book issued!")
                else:
                    print("Cannot issue!")

            elif choice == "3":
                isbn = input("Enter ISBN: ")
                book = lib.search_by_isbn(isbn)
                if book and book.return_book():
                    lib.save_data()
                    print("Book returned!")
                else:
                    print("Cannot return!")

            elif choice == "4":
                for b in lib.display_all():
                    print(b)

            elif choice == "5":
                t = input("Enter title keyword: ")
                result = lib.search_by_title(t)
                for r in result:
                    print(r)

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run()
