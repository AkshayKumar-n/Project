
bookslist=[]
class bookDetails:
    def AddBook(self,title,description,price,publisher,distributor):
        dict2={"title":title,"description":description,"price":price,"publisher":publisher,"distributor":distributor}
        bookslist.append(dict2)
obj1=bookDetails()



while(True):
    print("1. add book ")
    print("2. view book ")
    print("3. View all books in alphabetical order  ")
    print("4. search a book using title")
    print("5. exit")
    choice=int(input("Enter a choice: "))
    if choice==1:
            
            title=input("Enter title of book: ")
            description=input("Enter description of book: ")
            price=input("Enter price of book: ")
            distributor=input("Enter distributor of book: ")
            publisher=input("Enter publisher of book: ")


            obj1.AddBook(title,description,price,publisher,distributor)
            
    if choice==2:
        print(bookslist)
    if choice==3:
        print(sorted(bookslist,key=lambda i:i["title"]))
    if choice==4:
        search=input("Enter title to search product: ")
        print(list(filter(lambda a:a["title"]==search,bookslist)))
    if choice==5:
        break