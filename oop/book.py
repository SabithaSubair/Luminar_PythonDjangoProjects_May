# class Book:
#     def setval(self,book_name,author,pages,library_name):
#         self.book_name=book_name
#         self.author=author
#         self.pages=pages
#         self.library_name=library_name
#     def printval(self):
#         print("BooK Name::",self.book_name)
#         print("Author Name::",self.author)
#         print("BooK Pages::", self.pages)
#         print("Library Name::",self.library_name)
# ob=Book()
# ob.setval("ML","asd",20,"hjj")
# ob.printval()
# ob1=Book()
# ob1.setval("MLIL","asssd",2000,"hjj")
# ob1.printval()
#
#
# #read input from keyboard
# a=input("Enter the book name:")
# b=input("Enter the author name:")
# c=int(input("Enter the no of pages:"))
# d=input("Enter the book name:")
# ob.setval(a,b,c,d)
# ob.printval()

# if library is same use static variable
class Book:
    library_name="ab library"
    def setval(self,book_name,author,pages):
        self.book_name=book_name
        self.author=author
        self.pages=pages

    def printval(self):
        print("BooK Name::",self.book_name)
        print("Author Name::",self.author)
        print("BooK Pages::", self.pages)
        print("Library Name::",Book.library_name)
ob=Book()
ob.setval("ML","asd",20)
ob.printval()
ob1=Book()
ob1.setval("MLIL","asssd",2000)
ob1.printval()
#2 types of variables
#1...static variable..related to class....access using classnme
#2...instance variable..related to methods..access using self