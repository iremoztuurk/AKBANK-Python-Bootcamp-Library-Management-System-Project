import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import tkinter as tk
from tkinter import *
from datetime import datetime


def switch(operate):
    if operate == "1":
        lib.listcontent()
    elif operate == "2":
        info()
    elif operate == "3":
        removecont()
    elif operate == "4":
        showdetail()
    elif operate == "Q" or operate == "q":
        lib.__del__()
        quit()
    else:
        label = Label(main_window, text='Please input valid value..', font='Helvetica 9 bold', fg='red')
        label.place(y=320, x=50)


def submit_query():
    query = query_val.get()
    switch(query)


def createquery():
    global main_window, query_val
    main_window = Tk()
    label = Label(main_window, text="///Library Management System Menu///", font= 'Helvetica 16 bold italic')
    label_2 = Label(main_window, text="1) List Books", font= 'Helvetica 10 bold ')
    label_3 = Label(main_window, text="2) Add Books", font= 'Helvetica 10 bold')
    label_4 = Label(main_window, text="3) Remove Books", font= 'Helvetica 10 bold')
    label_5 = Label(main_window, text="4) List Detailed Info of a Book", font= 'Helvetica 10 bold')
    label_6 = Label(main_window, text="5) Q for QUIT", font= 'Helvetica 10 bold')

    query_val = Entry()

    label.place(y=50, x=50)
    label_2.place(y=100, x=50)
    label_3.place(y=125, x=50)
    label_4.place(y=150, x=50)
    label_5.place(y=175, x=50)
    label_6.place(y=200, x=50)
    query_val.place(y=250, x=50)

    button = Button(main_window, text="Submit", command = submit_query)
    button.place(x=50, y=280)

    main_window.geometry('500x400')
    main_window.title("Library Management System")
    main_window.mainloop()


def confirm_add(window):
    lib.addcontent(window)
    label = Label(window, text="Content is succesfully added!", font = 'Helvetica 10 bold italic', fg='blue')
    label.place(x=50, y=300)


def getinfo(window):
    current_datetime = datetime.now()
    yearinfo = current_datetime.year
    titles = title_info.get()
    authors = author_info.get()
    num_pages = num_page_info.get()
    release_dates = release_d_info.get()
    if not release_dates.isnumeric() or not num_pages.isnumeric() or int(release_dates) > yearinfo:
        window.destroy()
        info()
    return titles.title(), authors.title(), release_dates, num_pages


def info():
    global main_window2, title_info, author_info, release_d_info,num_page_info
    main_window2 = Tk()

    label = Label(main_window2, text="Title:", font='Helvetica 10')
    label_2 = Label(main_window2, text="Author:", font='Helvetica 10 ')
    label_3 = Label(main_window2, text="Release Date:", font='Helvetica 10 ')
    label_4 = Label(main_window2, text="Page Number:", font='Helvetica 10')

    title_info = Entry(main_window2)
    author_info = Entry(main_window2)
    release_d_info = Entry(main_window2)
    num_page_info = Entry(main_window2)

    label.place(x=50, y=50)
    label_2.place(x=50, y=100)
    label_3.place(x=50, y=150)
    label_4.place(x=50, y=200)

    title_info.place(x=175, y=50)
    author_info.place(x=175, y=100)
    release_d_info.place(x=175, y=150)
    num_page_info.place(x=175, y=200)

    button = Button(main_window2, text="Submit", command = lambda window=main_window2: confirm_add(window))
    button.place(x=50, y=250)

    main_window2.geometry('400x400')
    main_window2.title("Library Management System")
    main_window2.mainloop()


def confirm_rem(window):
    x = lib.removecontent()
    if x == 0:
        label = Label(window, text="This content is not available in database..", font='Helvetica 10 bold', fg = 'red')
        label.place(x=50, y=300)
    else:
        label = Label(window, text="Content is removed successfully..", font='Helvetica 10 bold', fg = 'blue')
        label.place(x=50, y=300)


def getremove():
    rem_titles = rem_title.get()
    return rem_titles.title()


def removecont():
    global main_window3, rem_title
    main_window3 = Tk()

    label = Label(main_window3, text="Title of the book\nto be removed:", font='Helvetica 10')

    rem_title = Entry(main_window3)

    label.place(x=50, y=50)
    rem_title.place(x=150, y=55)

    button = Button(main_window3, text="Submit", command= lambda window = main_window3 : confirm_rem(window))
    button.place(x=50, y=250)

    main_window3.geometry('300x400')
    main_window3.title("Library Management System")
    main_window3.mainloop()


def createtable(cols, data, headers, param):
    main_window1 = Tk()
    main_window1.geometry('600x500')
    main_window1.title('Library Management System')

    if not data:
        label = Label(main_window1, text="There is no content to be showed..", font='Helvetica 10 bold italic', fg='red')
        label.place(x=200, y=225)
        button = Button(main_window1, text="Back to Menu", command=main_window1.destroy)
        button.place(x=200, y=275)

    else:
        frame = Frame(main_window1)
        frame.pack(fill=BOTH, expand=1)

        canvas = Canvas(frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scroll = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        scroll.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scroll.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame2 = Frame(canvas)
        canvas.create_window((0, 0), window=frame2, anchor="nw")

        if param == 1:
            button2 = Button(main_window1, text="v",
                         command=lambda window=frame2: printing(cols, sorted(data, key=lambda w: w[0]), headers,
                                                                      window))
            button2.place(x=135, y=5)

            button3 = Button(main_window1, text="v",
                         command=lambda window=frame2: printing(cols, sorted(data, key=lambda w: w[1]), headers,
                                                                      window))
            button3.place(x=275, y=5)

        printing(cols, data, headers, frame2)


def printing(cols, data, headers, frame):

    for widget in frame.winfo_children():
        widget.destroy()

    i = 0
    for j, col in enumerate(headers):
        label = Label(frame, text=col.upper(), bg="#FA8072", font='Arial 10 bold ', borderwidth=1, relief="raised")
        label.grid(row=i, column=j, padx=5, pady=5)

    if len(data) == 4:
        i = 0
        for j in range(cols):
            label = Label(frame, text=data[j])
            label.grid(row=i+1, column=j, padx=8, pady=5)

    else:
        for i in range(len(data)):
            for j in range(cols):
                label = Label(frame, text=data[i][j])
                label.grid(row=i+1, column=j, padx=8, pady=5)

    frame.mainloop()


def getdetail(window):
    content = cont.get()
    x = lib.listcontentdetail(content)
    if x==0:
        label = Label(window, text="This content is not available in database..", font='Helvetice 10 bold', fg='red')
        label.place(x=50, y=100)


def showdetail():
    global main_window4, cont
    main_window4 = Tk()

    label = Label(main_window4, text = "Title of the content:")
    cont = Entry(main_window4)

    label.place(x=50, y=50)
    cont.place(x=175, y=50)

    button = Button(main_window4, text="Submit", command=lambda window=main_window4: getdetail(window))
    button.place(x=50, y=150)

    main_window4.geometry('400x200')
    main_window4.title("Library Management System")
    main_window4.mainloop()


class Library:
    def __init__(self):
        self.lib = open('book.txt', 'a+')
        self.title = str
        self.author = str
        self.release_date = str
        self.num_page = str
        self.content = []
        self.allContent = []
        self.contentremove = str
        self.newcontent = str
        self.listdetailcontent = str

    def addcontent(self, window):
        titles, authors, release_dates, num_pages = getinfo(window)
        self.content = titles + ',' + authors + ',' + str(release_dates) + ',' + str(num_pages)
        self.lib.write(self.content.strip() + "\n")
        self.lib.flush()

    def listcontent(self):
        self.lib.seek(0)
        self.allContent = self.lib.read()
        self.allContent = self.allContent.splitlines()
        headers = ['Title','Author']
        for i, sublists in enumerate(self.allContent):
            self.allContent[i] = self.allContent[i].split(',')
        param = 1
        createtable(2, self.allContent, headers , param)

    def listcontentdetail(self, cont):
        cont = cont.capitalize()
        self.lib.seek(0)
        self.allContent = self.lib.read()
        self.allContent = self.allContent.splitlines()
        headers = ['Title', 'Author', 'Release Date', 'Page Number']
        for i, sublists in enumerate(self.allContent):
            self.allContent[i] = self.allContent[i].split(',')
        a = 0
        for i, sublists in enumerate(self.allContent):
            if cont in self.allContent[i]:
                param = 0
                createtable(4, self.allContent[i], headers, param)
                a = a+1
                break
        return a

    def removecontent(self):
        rem_titles = getremove()
        self.lib.seek(0)
        self.allContent = self.lib.read()
        self.allContent = self.allContent.splitlines()
        for i, sublists in enumerate(self.allContent):
            self.allContent[i] = self.allContent[i].split(',')
        for i, sublists in enumerate(self.allContent.copy()):
            a=0
            if rem_titles in self.allContent[i][0]:
                self.allContent.pop(i)
                a = a+1
                break
        self.lib.seek(0)
        self.lib.truncate(0)
        for i, sublists in enumerate(self.allContent):
            self.newcontent = (self.allContent[i][0]+","+self.allContent[i][1]
                               + ","+self.allContent[i][2]+","+self.allContent[i][3])
            self.lib.write(self.newcontent + "\n")
        return a


    def __del__(self):
        self.lib.close()
        print("Library is closed..")


lib = Library()

while True:
    createquery()



