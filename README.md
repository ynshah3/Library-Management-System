# Library-Management-System
This program uses SQL to maintain a database of the details of books in the library and of the issuers of books from the library.

# About

I used PyMySQL to use SQL within Python and connect to a local host (on my computer). The program first asks the user if they want to continue as an Admin or as a customer. Continuing as an admin requires a password. The admin has priviledges that allow him to add or remove book from the library, get a list of all bokks, get details about a particular book, get information about customers who have issued books but haven't returned yet, etc. The customer, however, requires an ID (of the form A??) that was assigned to him when he opened an account with the library. He can check which books are available based on a particular genre of books, issue books, and return books. Books issued must be returned within 14 days of issuing to prevent late fees, and a customer cannot issue more than 3 books at a time (he can have a maximum of 3 issued books in his possession). 

# Project Significance

I developed this project because it allows me to get accustomed to databases, SQL, how SQL interacts with Python, and how large amounts of data is stored and retrieved.
