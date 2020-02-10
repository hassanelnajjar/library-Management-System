#classes
from datetime import date
class Book:
    def __init__(self,Book_Name,Book_Id ,Book_Type="True"):
        self.Book_Name = Book_Name
        self.Book_Type = Book_Type
        self.Book_Id = Book_Id
    
class Student:
    def __init__(self,Student_Name,Book_Name):
        self.Book_Name = Book_Name
        self.Student_Name = Student_Name

    def requestBook(self):
        return self.Book_Name

    def returnBook(self):
        return self.Book_Name

   
class library:
    def __init__(self,database=[]):
        self.database = database

    def borrow_Book(self,Book_Name,Student_Name):
        for book in self.database.get("Books"):
            if book.get("Book_Name") == Book_Name:
                book["Book_Type"] = "False"
                book["Student_Name"] = Student_Name
                book["Date"]=("{}-{}-{}".format(date.today().day,date.today().month,date.today().year))
        return self.database
        #Add Books Methods - request Book
    def add_Book(self,Book_Name,Student_Name):
        self.database.get("Books").append(
             {"Book_Name":Book_Name,
             "Book_Type":"True",
             "Student_Name" : Student_Name,
             "Date":("{}-{}-{}".format(date.today().day,date.today().month,date.today().year))
             })
        return self.database

    def add_Book_manger(self,Book_Name):
        self.database.get("Books").append(
             {"Book_Name":Book_Name,
             "Book_Type":"True",
             "Student_Name" : "",
             "Date":("{}-{}-{}".format(date.today().day,date.today().month,date.today().year))
             })
        return self.database
        #Update Books Method
    def updateBooks(self,Book_Name):
        for book in self.database.get("Books"):
            if book.get("Book_Name") == Book_Name:
                book["Book_Type"] = "True"
                book["Student_Name"]=""
                book["Date"] = ""
        return self.database
        #Display Availabe Books
    def displayBooks(self):
        for book in self.database.get("Books"):
            if book.get("Book_Type")=="True":
                print(book)
        #Display Borrowed Books
    def display_Bo_Books(self):
        for book in self.database.get("Books"):
            if book.get("Book_Type")=="False":
                print(book)
