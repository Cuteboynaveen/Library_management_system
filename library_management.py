class library:
    def __init__(self,name,x):
        self.library_name=library_name
        self.books_list=x
    def add_book(self,book_title):
        self.books_list.append(book_title)
        print(f"{book_title} is added")
    def remove_book(self,book_title):
        if book_title in self.books_list:
            self.books_list.remove(book_title)
            print(f"{book_title} is removed")
        else:
            print(f"{book_title} is not found")
    def search_book(self,book_title):
        if book_title in self.books_list:
            print(f"{book_title} is found")
        else:
            print(f"{book_title} is not found")
    def display_info(self):
        a=set(self.books_list)
        for i in a:
            print(f"{i} : {self.books_list.count(i)}")

library_name={"cse":["1","2","3"],"ece":["1","2","3"],"mech":["1","2","3"]}

name=input("enter the library name :")
if  name in library_name :
    lib=library(library_name,library_name[name])
    while(1):
        print(f"welcome {name.upper()}")
        choice=input("press any one\n 1.add \n 2.remove \n 3.search \n 4.display\n")
        if choice.upper() == "ADD" or choice.upper() =="1":
            book_name=input("title of the book")
            lib.add_book(book_name)
        elif choice.upper() =="REMOVE" or choice.upper() =="2":
            book_name=input("title of the book")
            lib.remove_book(book_name)
        elif choice.upper() =="SEARCH" or choice.upper() =="3":
            book_name=input("title of the book")
            lib.search_book(book_name)
        elif choice.upper() =="DISPLAY" or choice.upper() =="4":
            lib.display_info()
        else:
            print("invaild option")
        again=input("do you want to continue yes or no :")
        if again.upper() == "NO":
            break
else:
    print(f"{name} is not present")
    again =input("do you want continue yes or no:")
    if again.upper() == "YES":
        name = input("do you want to add library name:")
        books_list=list(map(int,input("enter the books to library").split()))
        library_name[name]=books_list
        print(library_name[name])

    



