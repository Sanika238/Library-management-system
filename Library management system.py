import os

with open("Library_Details1.txt", "a") as file:
    file.write("(Close this file to continue) "
               "\nCurrent list is as follows: \nID - NAME - PUBLISHER - AUTHOR - TOTAL QUANTITY\n")

BookID = [12424, 70387, 47851, 78852, 35651]
BookName = ["The Three Wolves", "Girl who went on", "Immortals of Meluha", "Interstellar Time", "A day in Metaverse"]
BookPublisher = ["Good Books", "Best Seller", "Westland Press", "International Journal of Books", "Meta Books"]
BookAuthor = ["Alan Watson", "Burns Scott", "Amish Tripathi", "Chris Lan", "Jann Martin"]
BookQty = [6, 3, 8, 10, 2]
CurrentQty = BookQty


def table_format(b_id, name, pub, auth, qty):
    with open("Library_Details1.txt", "a") as f:
        f.write(f"{b_id} | {name} | {pub} | {auth} | {qty}\n")


print("Current list is as follows: \n ID - NAME - PUBLISHER - AUTHOR - QUANTITY")
List_Books = list(map(table_format, BookID, BookName, BookPublisher, BookAuthor, BookQty))


def add_books():
    book_id = int(input("Enter Book ID: "))
    BookID.append(book_id)
    book_name = input("Enter Book Name: ")
    BookName.append(book_name)
    book_publisher = input("Enter Book Publisher: ")
    BookPublisher.append(book_publisher)
    book_author = input("Enter Book Author: ")
    BookAuthor.append(book_author)
    total_qty = int(input("Enter book's quantity: "))
    BookQty.append(total_qty)
    print("*** Book added successfully ***")
    table_format(book_id, book_name, book_publisher, book_author, total_qty)
    view_details()


def view_details():
    os.system("notepad Library_Details1.txt")
    main_menu()
    file.close()


def search_book(word):
    file_search = open("Library_Details1.txt", "r")
    f = 0
    ind = 0
    for line in file_search:
        ind += 1
        if word in line:
            f = 1
            break
    if f == 0:
        print("*** OOPS!", word, "not found in the list ***")
    else:
        print("*** Yay!", word, "found at index ", ind, " ***")
        view_details()
    main_menu()


def book_issue(id_ref):
    if book_available(id_ref):
        ind = BookID.index(id_ref)
        print("The number of these books available were:", CurrentQty[ind])
        CurrentQty[ind] -= 1
        print("Current quantity of the issued book:", CurrentQty[ind])
        view_details()
    else:
        print("Sorry! We do not have enough of the book you are looking for.")
    main_menu()


def book_available(id_ref):
    ind = BookID.index(id_ref)
    if CurrentQty[ind] > 1:
        return 1
    else:
        return 0


def book_return(id_ref):
    ind = BookID.index(id_ref)
    CurrentQty[ind] += 1
    print("The book returned was:", BookName[ind], "-", CurrentQty[ind])
    view_details()


def main_menu():
    print("-------------------------------------------------------------\n*** Main Menu ***")
    print("1• View the list of all books and their details"
          "\n2• Add books and their details"
          "\n3• Search for Book/Author"
          "\n4• Book issue"
          "\n5• Book return"
          "\n6• Check quantity"
          "\n7• Exit")
    inp = input("Enter the corresponding number: ")
    if inp == "1":
        view_details()
    elif inp == "2":
        add_books()
    elif inp == "3":
        word_search = input("Enter the Book or author name: ")
        search_book(word_search)
    elif inp == "4":
        id1 = int(input("Enter the Book ID: "))
        book_issue(id1)
    elif inp == "5":
        id2 = int(input("Enter the Book ID: "))
        book_return(id2)
    elif inp == "6":
        id2 = int(input("Enter the Book ID: "))
        try:
            BookID.index(id2)
            ind = BookID.index(id2)
            print("The quantity of this book is: ", BookQty[ind])
            main_menu()
        except ValueError:
            print("No such ID found")
            main_menu()
    elif inp == "7":
        open('Library_Details1.txt', 'w').close()
        exit(0)
    else:
        print("*** ERROR Please enter a valid number ERROR ***")
        main_menu()


main_menu()