import pymysql


def increment_count(isbn, count):
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            quantity = "SELECT `QUANTITY` from `Books` WHERE `ISBN` = %s"
            cursor.execute(quantity, (isbn,))
            result = cursor.fetchall()

        with connection.cursor() as cursor:
            update_book = "UPDATE `Books` SET `Quantity` = %s WHERE `ISBN` = %s"
            cursor.execute(update_book, (result[0][0] + count, isbn))
        connection.commit()
    finally:
        connection.close()


def add_book(isbn, name, author, genre, price, quantity=1):
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            insert_book = "INSERT INTO `Books` (ISBN, Name, Author, Genre, Price, Quantity) " \
                          "VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_book,
                           (isbn, name, author, genre,
                            price, quantity))
        connection.commit()
    finally:
        connection.close()


def get_details(isbn):
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            details = "SELECT * from `Books` WHERE `ISBN` = %s"
            cursor.execute(details, (isbn,))
            result = cursor.fetchall()
            print("\nISBN: {}".format(result[0][0]))
            print("Name: {}".format(result[0][1]))
            print("Author: {}".format(result[0][2]))
            print("Genre: {}".format(result[0][3]))
            print("Price: {}".format(result[0][4]))
            print("Quantity: {}".format(result[0][5]))
    finally:
        connection.close()


def remove_book(isbn):
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            exist_quantity = "SELECT `QUANTITY` from `Books` WHERE `ISBN` = %s"
            cursor.execute(exist_quantity, (isbn,))
            result = cursor.fetchall()

        with connection.cursor() as cursor:
            update = "UPDATE `Books` SET `Quantity` = %s WHERE `ISBN` = %s"
            cursor.execute(update, (result[0][0] - 1, isbn))
        connection.commit()
    finally:
        connection.close()


def change_price(isbn, new_price):
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            update = "UPDATE `Books` SET `Price` = %s WHERE `ISBN` = %s"
            cursor.execute(update, (new_price, isbn))
        connection.commit()
    finally:
        connection.close()


def get_list_of_books():
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            all_books = "SELECT * FROM `Books`"
            cursor.execute(all_books,)
            result = cursor.fetchall()
            print("\nISBN, Name, Author, Genre, Price, Quantity")
            print("------------------------------------------\n")
            for book in result:
                print(book)
    finally:
        connection.close()


def details_of_issued_books():
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            issued_books = '''SELECT `Books`.`ISBN`, `Books`.`Name`, `Books`.`Author`, 
                            `Issuers`.`ID`, `Issuers`.`Issuer_Name`, `Issuers`.`Issue_Date`
                            FROM `Books` 
                            JOIN `Issuers` 
                            ON `Books`.`ISBN` = `Issuers`.`Book_ISBN`
                            WHERE `Issuers`.`Return_Date` IS NULL AND `Issuers`.`Issue_Date` IS NOT NULL'''
            cursor.execute(issued_books, )
            result = cursor.fetchall()
            print("\nBook_ISBN, Book_Name, Book_Author, Issuer_ID, Issuer_Name, Issue_Date")
            print("---------------------------------------------------------------------\n")
            for book in result:
                print("{}, {}, {}, {}, {}, {}"
                      .format(book[0], book[1], book[2], book[3], book[4], book[5].strftime('%Y-%m-%d')))
    finally:
        connection.close()


def count_books():
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            count = "SELECT SUM(`Quantity`) FROM `Books`"
            cursor.execute(count, )
            result = cursor.fetchall()
            print("\nCount of books currently in the Library: {}".format(result[0][0]))
    finally:
        connection.close()


def issuers_of_book(isbn):
    connection = pymysql.connect(read_default_file="~/.my.cnf")
    try:
        with connection.cursor() as cursor:
            issuers = '''SELECT `Issuers`.`ID`, `Issuers`.`Issuer_Name`, `Issuers`.`Issue_Date`
                        FROM `Books` 
                        JOIN `Issuers` 
                        ON `Books`.`ISBN` = `Issuers`.`Book_ISBN`
                        WHERE `Books`.`ISBN` = %s'''
            cursor.execute(issuers, (isbn,))
            result = cursor.fetchall()
            print("\nIssuer_ID, Issuer_Name, Issue_Date")
            print("----------------------------------\n")
            for query in result:
                print("{}, {}, {}".format(query[0], query[1], query[2].strftime('%Y-%m-%d')))
    finally:
        connection.close()
