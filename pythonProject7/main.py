from tkinter import *


def GO():
    teamp = Tk()
    teamp.title("BDeep Teams : Home Page")
    teamp.geometry("800x600")
    teamp.mainloop()

loginpage = Tk()
loginpage.title("BDeepTech: Teams")
loginpage.geometry("600x400")
loginpage.resizable(0,0)
loginpage.iconbitmap('favicon (2).ico')
txt1 = Label(loginpage, text="login to acces BDeep Tech Teams")
txt1.config(font=(44))
txt1.pack()

test = Label(loginpage, text="")
test.pack()

test2 = Label(loginpage, text="")
test2.pack()getint

test3 = Label(loginpage, text="")
test3.pack()

test4 = Label(loginpage, text="")
test4.pack()


txt2 = Label(loginpage, text="Email:")
txt2.pack()

in1 = Entry(loginpage, width=30)
in1.pack()


txt2 = Label(loginpage, text="Password:")
txt2.pack()

in1 = Entry(loginpage, width=30)
in1.pack()





test5 = Label(loginpage, text="")
test5.pack()

btn1 = Button(loginpage, text="Login", command=GO)
btn1.pack()

loginpage.mainloop()

txt2 = Label(loginpage, text="CEO:Bhavdeep saragadam:")
txt2.pack()