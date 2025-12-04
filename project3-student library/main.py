class library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    def displayAvailableBooks(self):
       print("Books present in the library are:")
       for book in self.books:
           print("\t *" + book)
    def borrowBoook(self,bookName) :
        if bookName in self.books:
            print(f"you have been issued {bookName}.Please keep it safe and return it with in 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry,This book is either unavialable or has been already issued to someone else.please,wait until the book is availabe")
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book")        
class student:
    def requestBook(self):
        self.book=input("enter the name of the book you want to borrow:\n")
        return self.book

    def returnBook(self):
       self.book=input("enter the name of the book you want to return:\n")
       return self.book
if __name__=="__main__" :
    centralLibrary=library(["Python","Django","c++","Data Structure"])
    student = student()
    #centralLibrary.displayAvailableBooks()
    while(True):
        welcomemsg='''
        ****Welcome To The Central Library****
        Please choose an option:
        1.List all the boooks
        2.Request a book
        3.Add/Return the book
        4.Exit the library'''
        a=int(input("enter the choice:"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBoook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing this Library!")
            exit()
        else:
            print("Invalid choice!")
        print(welcomemsg)