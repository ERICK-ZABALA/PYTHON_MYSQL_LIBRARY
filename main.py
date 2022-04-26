
import mysql.connector
from discount import discountBook
import mysql.connector

titleIdBook = "Id:"
titleNameBook = "Name Book:"
titleIsbnBook = "ISBN:"
titlePriceBook = "Price:"
titleGenreBook = "Genre:"



def showMenuGetChoice():

    print("1. Insert Book ")
    print("2. Display Book ")
    print("3. Update Book ")
    print("4. Delete Book ")
    print("5. Search Book by ISBN: ")
    print("6. Search Book by Genre: ")
    print("7. Exit")

    choice = int(input("Enter the choice: "))

    return choice


def insertBook():
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testpy"

    )

    myCursor = connection.cursor()
    idBook = int(input("Enter the Id Book:"))
    nameBook = (input("Enter the Name Book:")).strip()
    authorBook = (input("Enter the Author Book:")).strip()
    descriptionBook = (input("Enter the Description Book:")).strip()
    isbnBook = (input("Enter the ISBN Book (XXX-1449355730):")).strip()
    priceBook = float(input("Enter the Price Book:"))
    genreBook = (input("Enter the Genre Book (IT, Novel, Science):")).strip()

    insertQuery = "INSERT INTO ebook (Id, Name, Author, Description, Isbn, Price, Genre) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (idBook, nameBook, authorBook, descriptionBook, isbnBook, priceBook, genreBook)
    myCursor.execute(insertQuery, values)
    connection.commit()
    print("\n", myCursor.rowcount, "Records inserted")
    connection.close()

def displayBook():
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testpy"

    )

    myCursor = connection.cursor()

    selectQuery = "SELECT * FROM eBook"
    myCursor.execute(selectQuery)
    for row in myCursor:
        print ("%s %-4s %-11s %-38s %-5s %-14s %s %-4s" %(titleIdBook,row[0],
        titleNameBook,row[1],titleIsbnBook,row[4],titlePriceBook,row[5]))
        #print ("ID: ", row[0] , "Book Name: ", row[1] , "ISBN: ", row[4])

    connection.close()



def updateBook():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testpy"

    )


    myCursor = connection.cursor()

    idBook = int(input("Enter Id Book:"))
    nameBook = (input("Enter the Name Book:")).strip()
    authorBook = (input("Enter the Author Book:")).strip()
    descriptionBook = (input("Enter the Description Book:")).strip()
    isbnBook = (input("Enter the Isbn Book:")).strip()
    priceBook = (input("Enter the Price Book:")).strip()
    genreBook = (input("Enter the Genre Book:")).strip()

    #UPDATE Customers SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' WHERE CustomerID = 1;
    updateQuery = f"UPDATE eBook SET Id = '{idBook}', Name= '{nameBook}', Author= '{authorBook}'" \
                  f", Description= '{descriptionBook}', Isbn= '{isbnBook}', Price= '{priceBook}'" \
                  f", Genre= '{genreBook}' WHERE Id = '{idBook}'"

    myCursor.execute(updateQuery)
    connection.commit()

    if (myCursor.rowcount > 0):

        print((myCursor.rowcount, "Records Update"))

    else:

        print("eBook ID not found")

    # SELECT * FROM Customers WHERE Country='Mexico';
    selectQuery = f"{'SELECT * FROM ebook WHERE Id='}'{idBook}'"
    #print (selectQuery)
    myCursor.execute(selectQuery)
    for row in myCursor:
        print("%s %-4s %-11s %-38s %-5s %-14s %s %-6s %s %-4s" % (titleIdBook, row[0],
        titleNameBook, row[1], titleIsbnBook, row[4], titleGenreBook, row[6], titlePriceBook,row[5]))

    connection.close()



def deleteBook():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testpy"

    )

    myCursor = connection.cursor()
    idBook = int(input("Enter the ID Book to delete:  "))
    deleteQuery = "DELETE From eBook WHERE id=%s"
    values = (idBook,)
    myCursor.execute(deleteQuery, values)
    connection.commit()

    if (myCursor.rowcount > 0):

        print(myCursor.rowcount, "records deleted")

    else:

        print("Book Id not founded")

    connection.close()


def searchBookIsbn():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testpy"

    )

    myCursor = connection.cursor()

    isbnBook = input("Enter the ISBN Book (XXX-1449355730): ")
    # SELECT * FROM Customers WHERE Country='Mexico';
    selectQuery = f"{'SELECT * FROM ebook WHERE Isbn='}'{isbnBook}'"
    #print (selectQuery)
    myCursor.execute(selectQuery)

    for row in myCursor:
         print("%s %-4s %-11s %-38s %-5s %-14s %s %-6s %s %-4s" % (titleIdBook, row[0],
         titleNameBook, row[1], titleIsbnBook, row[4],
         titleGenreBook, row[6], titlePriceBook, row[5]))
         # print ("ID: ", row[0] , "Book Name: ", row[1] , "ISBN: ", row[4])

    connection.close()

def searchBookGenre():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testpy"

    )

    myCursor = connection.cursor()

    genreBook = input("Enter the Genre Book (IT,Novel,Science): ")
    # SELECT * FROM Customers WHERE Country='Mexico';
    selectQuery = f"{'SELECT * FROM ebook WHERE Genre='}'{genreBook}'"
    #print (selectQuery)
    myCursor.execute(selectQuery)
    for row in myCursor:
        newDiscountPrice = discountBook(row[5])
        formatNewDiscountPrice = "{:.2f}".format(newDiscountPrice)
        print("%s %-4s %-11s %-28s %-5s %-14s %s %-6s %s %-4s" % (titleIdBook, row[0],
        titleNameBook, row[1], titleIsbnBook, row[4], titleGenreBook, row[6],
        titlePriceBook,formatNewDiscountPrice + ' US$' ))
        # print ("ID: ", row[0] , "Book Name: ", row[1] , "ISBN: ", row[4])

    connection.close()


while (True):

    try:

        choice = showMenuGetChoice()

        if choice == 1:
             insertBook()
             input("Press any letter to continue ...\n")
        elif choice == 2:
            displayBook()
            input("Press any letter to continue ...\n")
        elif choice == 3:
            updateBook()
            input("Press any letter to continue ...\n")
        elif choice == 4:
             deleteBook()
             input("Press any letter to continue ...\n")
        elif choice == 5:
            searchBookIsbn()
            input("Press any letter to continue ...\n")
        elif choice == 6:
            searchBookGenre()
            input("Press any letter to continue ...\n")
        elif choice == 7:
            print("Thank You, Have a good Day :) !!!")
            break
        else:
            print("Invalid Option, insert correct option !!!")

    except:
        print("Invalid Option, insert correct option !!!")


