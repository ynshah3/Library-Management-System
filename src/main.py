from Books import *
from Issuers import Issuer
import sys


def main():
    print("\nWelcome to XYZ Library!\n\n")
    choice = int(input("To continue as admin, type 1; to continue as customer, type 2:"))
    if choice not in {1, 2}:
        print("\nxxx Incorrect choice xxx")
        print("Exiting...")
        sys.exit(1)
    elif choice == 1:
        pwd = input("\nEnter password to continue: ")
        if pwd != "Lgn!As@Admn2Lib%":
            print("\nxxx Incorrect password xxx")
            print("Exiting...")
            sys.exit(1)
        else:
            print("\nHello :)\n")
            ans = True
            while ans is not False:
                print("\n---Main Menu---\n")
                print("1. Add a new book")
                print("2. Add an existing book")
                print("3. Get details about a book")
                print("4. Update price of a book")
                print("5. Get details about all books in the library")
                print("6. Get details about books currently issued")
                print("7. Total number of books in the library")
                print("8. Get list of all issuers of a particular book who haven't yet returned their issued books")
                print("9. Remove single copy of book\n")
                choice2 = int(input("Enter your choice (1-9): "))
                print()
                if choice2 == 1:
                    isbn = int(input("Enter ISBN of Book: "))
                    name = input("Enter Name of Book: ")
                    author = input("Enter Author of Book: ")
                    genre = input("Enter Genre of Book (Action/Adventure/Comedy/Romance/Sci-Fi/etc.): ")
                    price = float(input("Enter Price of Book as decimal up to 2 places (without $ sign): "))
                    quantity = int(input("Enter Quantity of Books to be added: "))
                    add_book(isbn, name, author, genre, price, quantity)
                elif choice2 == 2:
                    isbn = int(input("Enter ISBN of Book: "))
                    count = int(input("Enter Quantity of Books to be added: "))
                    increment_count(isbn, count)
                elif choice2 == 3:
                    isbn = int(input("Enter ISBN of Book: "))
                    get_details(isbn)
                elif choice2 == 4:
                    isbn = int(input("Enter ISBN of Book: "))
                    price = float(input("Enter new Price of Book as decimal up to 2 places (without $ sign): "))
                    change_price(isbn, price)
                elif choice2 == 5:
                    get_list_of_books()
                elif choice2 == 6:
                    details_of_issued_books()
                elif choice2 == 7:
                    count_books()
                elif choice2 == 8:
                    isbn = int(input("Enter ISBN of Book: "))
                    issuers_of_book(isbn)
                elif choice2 == 9:
                    isbn = int(input("Enter ISBN of Book: "))
                    remove_book(isbn)
                else:
                    print("\nxxx Incorrect choice xxx")
                    print("Exiting...")
                    sys.exit(1)
                print()
                get_ans = input("Do you want to exit? (yes/no): ")
                print()
                ans = False if get_ans.lower() == "yes" else True
    elif choice == 2:
        print("\nHello :)\n")
        name = input("Enter your Full Name: ")
        issuer_id = input("Enter your id (should be of the form A followed by 2 digits:) ")
        i_obj = Issuer(issuer_id, name)
        ans = True
        while ans is not False:
            print("\n---Main Menu---\n")
            print("1. Issue a book")
            print("2. Return an issued book")
            print("3. Get list of books available for issuing\n")
            choice2 = int(input("Enter your choice (1-3): "))
            print()
            if choice2 == 1:
                isbn = int(input("Enter ISBN of Book you want to issue: "))
                i_obj.issue_book(isbn)
            elif choice2 == 2:
                isbn = int(input("Enter ISBN of Book you want to return: "))
                i_obj.return_book(isbn)
            elif choice2 == 3:
                genre = input("Enter a genre from which you want to see available books "
                              "(eg. Action, Comedy, Romance): ")
                i_obj.get_available_books(genre.capitalize())
            else:
                print("\nxxx Incorrect choice xxx")
                print("Exiting...")
                sys.exit(1)
            print()
            get_ans = input("Do you want to exit? (yes/no): ")
            print()
            ans = False if get_ans.lower() == "yes" else True
    print()
    print("Thanks for visiting!")
    print("\nBye...")


if __name__ == '__main__':
    main()
