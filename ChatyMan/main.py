#ChatServer
from tkinter import *
import random

def ChatServer():
    root = Tk()
    root.title(f"ChatyMan : ChatServer")
    root.geometry("300x500")
    root.iconbitmap('favicon (2).ico')
    def sent():
        txt = Label(root, text=in1.get())
        txt1 = Label(root, text=user.get() + " :")
        txt1.pack()
        in1.delete(0, END)
        txt.pack()




    guicode = Label(root, text="Chaty Code : " + str(random.randint(1, 10100)))
    guicode.pack()

    txt2 = Label(root, text="Enter Your Username")
    txt2.pack()

    user = Entry(root, width=100, borderwidth=10)
    user.pack()

    test = Label(root, text=" ")
    test.pack()

    txt3 = Label(root, text="Type Below To Send")
    txt3.pack()

    in1 = Entry(root, width=100, borderwidth=10)
    in1.pack(ipady=5)

    btn1 = Button(root, text="Send", command=sent)
    btn1.pack(ipadx=300)

    root.mainloop()
Home = Tk()
Home.title("ChatyMan : Home")
Home.geometry("600x500")
Home.iconbitmap('favicon (2).ico')
Home.config(bg=("sky blue"))

title = Label(Home, text="ChatyMan")
title.config(font=(44))
title.pack()

test1 = Label(Home, text=" ")
test1.pack()

test2 = Label(Home, text=" ")
test2.pack()

test3 = Label(Home, text=" ")
test3.pack()

test4 = Label(Home, text=" ")
test4.pack()

label1 = Label(Home, text="Create a Chaty Server")
label1.config(font=(44))
label1.pack()

test5 = Label(Home, text=" ")
test5.pack()

btncreate = Button(Home, text="Create", command=ChatServer)
btncreate.pack(ipadx=50, ipady=50)



test6 = Label(Home, text=" ")
test6.pack()

test7 = Label(Home, text=" ")
test7.pack()

test8 = Label(Home, text=" ")
test8.pack()
label2 = Label(Home, text="Join a Chaty Server")
label2.config(font=(44))
label2.pack()

label4 = Label(Home, text="Enter The Chaty Code To Join")

joins = Entry(Home, width=50)
joins.pack()




Home.mainloop()