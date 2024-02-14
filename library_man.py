import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import tkinter as tk
from tkinter import *

def switch(operate):
    if operate == "1":
        books.listcontent()
    elif operate == "2":
        books.addcontent()
    elif operate == "3":
        books.removecontent()
    elif operate == "4":
        books.listcontentdetail()
        #clear all data da ekle***************

def submit_query(query_val):
    query = query_val.get()
    main_window.destroy()
    return query

def createquery():
    global main_window
    main_window = Tk()
    query = int
    label = Label(main_window, text="Library Management System Menu")
    label_2 = Label(main_window, text="1)List Books")
    label_3 = Label(main_window, text="2)Add Books")
    label_4 = Label(main_window, text="3)Remove Books")
    label_5 = Label(main_window, text="4)List Detailed Info of a Book")
    label_6 = Label(main_window, text="5)Remove all data from database")
    label_7 = Label(main_window, text="6)Q for QUIT")

    global query_val
    query_val = Entry()
    label.place(y=50, x=50)
    label_2.place(y=75, x=50)
    label_3.place(y=100, x=50)
    label_4.place(y=125, x=50)
    label_5.place(y=150, x=50)
    label_6.place(y=175, x=50)
    label_7.place(y=200, x=50)
    query_val.place(y=225, x = 50)


    button = Button(main_window, text = "Submit", command = lambda: submit_query)
    button.place(x= 50, y = 260)

    main_window.geometry('700x300')
    main_window.title("Library Management System")
    main_window.mainloop()
    return query_val

def createtable(cols,data,headers):
    window = Tk()
    window.geometry('600x500')
    window.title('Library Management System')
    i = 0
    for j, col in enumerate(headers):
        text = Text(window, width=12, height=1, bg = "#9BC2E6")
        text.grid(row=i,column=j)
        text.insert(INSERT, col)

    if len(data) == 4:
        i=0
        for j in range(cols):
            text = Text(window, width=16, height=1)
            text.grid(row=i + 1, column=j)
            text.insert(INSERT, data[j])

    else:
        for i in range(len(data)):
            for j in range(cols):
                text = Text(window, width=16, height=1)
                text.grid(row=i + 1, column=j)
                text.insert(INSERT, data[i][j])

    window.mainloop()



class Library:
    def __init__(self):
        self.book = open('book.txt', 'a+')
        self.title = str
        self.author = str
        self.release_date = str
        self.num_page = str
        self.content = []
        self.allContent = []
        self.contentremove = str
        self.newcontent = str
        self.deletedcont = []
        self.listdetailcontent = str

    def addcontent(self):
        self.title = input("Title:\n").capitalize()
        self.author = input("Author:\n").capitalize()
        self.release_date = input("Release Year:\n")
        self.num_page = input("Number of Page:\n")
        self.content = self.title + ',' + self.author + ',' + str(self.release_date) + ',' + str(self.num_page)
        self.book.write(self.content.strip() + "\n")
        self.book.flush()

    def listcontent(self):
        self.book.seek(0)
        self.allContent = self.book.read()
        self.allContent = self.allContent.splitlines()
        headers = ['Title','Author']
        #print('****Titles*****Author****')
        for i, sublists in enumerate(self.allContent):
            self.allContent[i] = self.allContent[i].split(',')
        createtable(2, self.allContent, headers)
        """
            print(f'{self.allContent[i][0]}    {self.allContent[i][1]}')
            if not self.allContent:
              print("Content is empty..")"""
        #createGUI(len(self.allContent), 2, self.allContent,headers)

    def listcontentdetail(self):
        self.listdetailcontent = input("Please input the title of the book you want to list detailed info:\n")
        self.book.seek(0)
        self.allContent = self.book.read()
        self.allContent = self.allContent.splitlines()
        headers = ['Title', 'Author', 'Release Date', 'Page Number']
        for i, sublists in enumerate(self.allContent):
            self.allContent[i] = self.allContent[i].split(',')

        #createGUI(len(self.allContent),4,self.allContent,headers)
        for i, sublists in enumerate(self.allContent):
            if self.listdetailcontent in self.allContent[i]:
                print(self.allContent[i])
                createtable(4, self.allContent[i], headers)
                break
            else:
                print("This content is not available in database")

    def removecontent(self):
        self.contentremove = input("Please input the title of the book you want to delete from the database:\n ").capitalize()
        self.book.seek(0)
        self.allContent = self.book.read()
        self.allContent = self.allContent.splitlines()
        for i, sublists in enumerate(self.allContent):
            self.allContent[i] = self.allContent[i].split(',')
        for i, sublists in enumerate(self.allContent.copy()):
            if self.contentremove in self.allContent[i][0]:
                self.allContent.pop(i)
                print("Desired content is deleted..")
                self.deletedcont.append(self.contentremove)
                break
            else:
                print("This content is not found in the database..")
        self.book.seek(0)
        self.book.truncate(0)
        for i, sublists in enumerate(self.allContent):
            self.newcontent = (self.allContent[i][0]+","+self.allContent[i][1]
                               + ","+self.allContent[i][2]+","+self.allContent[i][3])
            self.book.write(self.newcontent + "\n")

    def __del__(self):
        self.book.close()
        print("Library is closed..")


books = Library()

while True:
    operation = createquery()
    if operation == "Q":
        break
    switch(operation)
