#library Management System :-
from clas_ob import library, Student,Book

LibraryDataBase = {"Books":[
{"Book_Name" :"1","Book_Type":"True","Student_Name" : "","Date":""},
{"Book_Name":"2","Book_Type":"True","Student_Name" : "","Date":""},
{"Book_Name":"3","Book_Type":"False","Student_Name" : "Hassan","Date":"5-2-2020"},
{"Book_Name":"4","Book_Type":"True","Student_Name" : "","Date":""},
{"Book_Name":"5","Book_Type":"False","Student_Name" : "Mohammed","Date":"10-2-2020"},
{"Book_Name":"6","Book_Type":"True","Student_Name" : "","Date":""},
]
}
# Main Function :-
def main():
    print("Please Choose one of the following :-")
    student_or_manager = int(input("Login as 1. sudents or 2. Manger or 3. Exit :-"))
    L1=library(LibraryDataBase)
    if student_or_manager == 1:
        student_options = int(input("1. Requst Book :\n2. return a Book :\n ..."))
        Student_Name = input("Enter Your Name :")
        Book_Name = input("Enter the book name :")
        
        Student_Object = Student(Student_Name,Book_Name)
        
        if student_options == 1:#request book - lend method
            Wanted_Book = Student_Object.requestBook()
            L1.borrow_Book(Wanted_Book,Student_Object.Student_Name)
        
        elif student_options == 2:#return book - update method
            Wanted_Book = Student_Object.requestBook()
            L1.updateBooks(Wanted_Book)
        
        else:
            print("Please Enter 1 or 2 only :) ...")
    elif student_or_manager == 2:
        Manager_options = int(input("1. Display Available Books : \n2. Display borrowed Books : \n3. Add Books : \n ..."))
        
        if Manager_options == 1:
            L1.displayBooks()

        elif Manager_options==3 :
            Wanted_Book = input("Enter Book Name : ")
            L1.add_Book_manger(Wanted_Book)

        elif Manager_options==2:
            L1.display_Bo_Books()
            
    elif student_or_manager == 3:
        return
    main()
main()
