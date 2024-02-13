class Library:
    def __init__(self):
        self.book = open('book.txt', 'a+')
        self.title = str
        self.author = str
        self.release_date = int
        self.num_page = int
        self.content = []
        self.allContent = []
        self.contentremove = str
        self.newcontent = str

    def addcontent(self):
        self.title = input("Title:\n").capitalize()
        self.author = input("Author:\n").capitalize()
        self.release_date = str(input("Release Year:\n"))
        self.num_page = str(input("Number of Page:\n"))
        self.content = self.title + ',' + self.author + ',' + self.release_date + ',' + self.num_page
        self.book.write(self.content.strip()+"\n")

    def listcontent(self):
        self.book.seek(0)
        self.allContent = self.book.read()
        self.allContent = self.allContent.splitlines()
        print(self.allContent)
        print('****Titles*****Author****')
        for i, sublists in enumerate(self.allContent):
            self.allContent[i] = self.allContent[i].split(',')
            """        for i, lines in enumerate(self.allContent):
            self.allContent[i] = lines.split(' ')"""
            print(f'{self.allContent[i][0]}    {self.allContent[i][1]}')
        if not self.allContent:
            print("Content is empty..")

    def removecontent(self):
        self.contentremove = input("Please input the title of the book you want to delete from the database:\n ")
        self.book.seek(0)
        self.allContent = self.book.read()
        self.allContent = self.allContent.splitlines()
        print("****")
        print(self.allContent)
        for i, sublists in enumerate(self.allContent):
            self.allContent[i] = self.allContent[i].split(',')
        for i, sublists in enumerate(self.allContent.copy()):
            if self.contentremove in sublists:
                self.allContent.pop(i)
            else:
                print("This content is not found in the database..")
        print(self.allContent)
        self.book.seek(0)
        self.book.truncate(0)
        for i, sublists in enumerate(self.allContent):
            self.newcontent = (self.allContent[i][0]+","+self.allContent[i][1]
                               + ","+self.allContent[i][2]+","+self.allContent[i][3]+" ")
            self.book.write(self.newcontent)

    def __del__(self):
        self.book.close()
        print("Library is closed..")


books = Library()


def switch(operate):
    if operate == "1":
        books.listcontent()
    elif operate == "2":
        books.addcontent()
    elif operate == "3":
        books.removecontent()


while True:
    operation = input("***MENU***\n1)List Books\n2)Add Books\n3)Remove Books\n4)Q for QUIT\n")
    if operation == "Q":
        break
    switch(operation)
