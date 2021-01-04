import pymysql
from Books import increment_count
from Books import remove_book
from datetime import date


class Error(Exception):
    pass


class IssueError(Error):
    def __init__(self, message):
        self.message = message


class Issuer:
    def __init__(self, issuer_id, name):
        self.issuer_id = issuer_id
        self.name = name

    def get_name(self):
        return self.name

    def get_available_books(self, genre):
        print("\n{}, available books of your chosen genre are:".format(self.name))
        print()
        connection = pymysql.connect(read_default_file="~/.my.cnf")
        try:
            with connection.cursor() as cursor:
                book_list = "SELECT `ISBN`, `Name`, `Author` FROM `Books` WHERE `Genre` = %s AND `Quantity` > 0"
                cursor.execute(book_list, (genre,))
                result = cursor.fetchall()
                print("ISBN: Book Name, by Author")
                print("--------------------------\n")
                for book in result:
                    print("{}: {}, by {}".format(book[0], book[1], book[2]))
        finally:
            connection.close()

    def issue_book(self, isbn):
        result = []
        tmp: tuple = (0,)
        result.append(tmp)
        book = isbn
        connection = pymysql.connect(read_default_file="~/.my.cnf")
        try:
            with connection.cursor() as cursor:
                count = "SELECT COUNT(*) FROM `Issuers` WHERE `ID` = %s AND `Return_Date` IS NULL"
                cursor.execute(count, (self.issuer_id,))
                result = cursor.fetchall()
                if result[0][0] >= 3:
                    raise IssueError("\nYou cannot issue any more books at the moment. "
                          "Please return at least one of your issued books before continuing.\n")

            with connection.cursor() as cursor:
                while result[0][0] == 0:
                    exist_quantity = "SELECT `Quantity` FROM `Books` WHERE `ISBN` = %s"
                    cursor.execute(exist_quantity, (isbn,))
                    result = cursor.fetchall()
                    if result[0][0] == 0:
                        print("\nNo book with the associated ISBN is available for rental at the moment. Sorry :(\n")
                        book = int(input("Enter another ISBN: "))

            with connection.cursor() as cursor:
                print("\nYou must return within 14 days of issuing!\n")
                issue_date = date.today().strftime('%Y-%m-%d')
                issue = "INSERT INTO `Issuers` (`ID`, `Issuer_Name`, `Book_ISBN`, `Issue_Date`) VALUES (%s, %s, %s, %s)"
                cursor.execute(issue, (self.issuer_id, self.name, book, issue_date))
            connection.commit()

            remove_book(book)

        except IssueError as ie:
            print(ie.message)
        finally:
            connection.close()

    def return_book(self, isbn):
        today_date = date.today().strftime('%Y-%m-%d')
        connection = pymysql.connect(read_default_file="~/.my.cnf")
        try:
            with connection.cursor() as cursor:
                issue_date = "SELECT `Issue_Date` FROM `Issuers` WHERE `ID` = %s AND `Book_ISBN` = %s"
                cursor.execute(issue_date, (self.issuer_id, isbn))
                result = cursor.fetchall()
                if today_date > (result[0][0]).strftime('%Y-%m-%d'):
                    print("\nYou are late in returning your rented book! Please settle your late fine with an admin\n")

            with connection.cursor() as cursor:
                update = "UPDATE `Issuers` SET `Return_Date` = %s WHERE `ID` = %s AND `Book_ISBN` = %s"
                cursor.execute(update, (today_date, self.issuer_id, isbn))
            connection.commit()

            increment_count(isbn, 1)
        finally:
            connection.close()
