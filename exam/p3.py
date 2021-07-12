class Book:
    def setval(self,library_name,book_name,author,pages):
        self.library_name = library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages

    def printval(self):
        print("Library Name::", self.library_name)
        print("BooK Name::",self.book_name)
        print("Author Name::",self.author)
        print("BooK Pages::", self.pages)

ob=Book()
ob.setval("abcd library","ML","asd",20)
ob.printval()
ob1=Book()
ob1.setval("zxcv library","MLIL","asssd",2000)
ob1.printval()