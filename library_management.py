class Library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lendDict={}
        
    def displayBooks(self):
        print("We have following books in our library : {}".format(self.name))
        for i in self.bookslist:
            print(i)
    
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book data has been updated")
        else:
            print("Book is already being used by {} ".format(self.lendDict[book]))
    
    def addBook(self,book):
        self.bookslist.append(book)
        print("book has been added to the booklist")
    
    def returnBook(self,book):
        self.lendDict.pop(book)
    
    
if __name__== '__main__':
    manas = Library(['python','rich dad- poor dad',"Harry potter","subbtle art"],"Manas")
    
    while(True):
        print("Welcome to the {} library. Enter your choice to continue!".format(manas.name))
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
	  if user_choice not in ['1','2','3','4']:
		print("Please enter a valid option!!")
		continue
	  else:
		user_choice = int(user_choice)
        
        if user_choice==1:
            manas.displayBooks()
        elif user_choice==2:
            book = input("Enter the name of the book you want to lend : ")
            user = input("Enter your name : ")
            manas.lendBook(user,book)
        elif user_choice==3:
            book = input("Enter the name of the book you want to add :")
            manas.addBook(book)
        elif user_choice==4:
            book = input("Enter the name of the book you want to return:")
            manas.returnBook(book)
        else:
            print("Not a valid option")
            
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!='c' and user_choice2!='q'):
            user_choice2 = input()
           
            if user_choice2=='q':
                exit()
            elif user_choice2=='c':
                continue
            
            
        
        
    