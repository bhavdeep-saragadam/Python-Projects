from tkinter import *

root = Tk()
root.title("Test : Id Page")
root.geometry("300x500")
root.iconbitmap('favicon (7).ico')
root.config(bg=("orange"))



def Next2():
    
    root.title("Quetion 1 MATH")
    txt1.pack_forget()
    txt2.pack_forget()
    btn2.pack_forget()

    txt3 = Label(root, text="What Is 5 Times 5", font="10", bg="orange")
    txt3.pack()

    test10 = Label(root, bg="orange")
    test10.pack()





def Next1():
    global txt1
    global txt2
    global btn2

    root.title("Test Read")
    title.pack_forget()
    idtxt.pack_forget()
    idin.pack_forget()
    btn1.pack_forget()

    txt1 = Label(root, text="This is the MATH", fg="red")
    txt1.config(font=(44))
    txt1.pack()

    txt2 = Label(root, text="test this shows your knowledge", fg="red" ,font=44)
    txt2.pack()

    test9 = Label(root, bg="orange")
    test9.pack()
    btn2 = Button(root, text="Next", borderwidth=0, command=Next2)
    btn2.pack(ipadx=10, ipady=10)

title = Label(root, text="Id Page", bg="orange", font=40)
title.pack()

test1 = Label(root, bg="orange")
test1.pack()



test2 = Label(root, bg="orange")
test2.pack()

test3 = Label(root, bg="orange")
test3.pack()

test4 = Label(root, bg="orange")
test4.pack()

test5 = Label(root, bg="orange")
test5.pack()

test6 = Label(root, bg="orange")
test6.pack()

idtxt = Label(root, text="Your Name : ", bg="orange", font=10)
idtxt.pack()

test7 = Label(root, bg="orange")
test7.pack()

idin = Entry(root, width=30, borderwidth=0)
idin.pack(ipady=5)


test8 = Label(root, bg="orange")
test8.pack()

btn1 = Button(root, text="Next", borderwidth=0, command=Next1)
btn1.pack(ipadx=10, ipady=10)

root.mainloop()

