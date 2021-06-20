from tkinter import *
import random
root = Tk()
root.title("Taable 2.0")
root.geometry("800x600")
root.resizable(False,False)
def DeleteTab():
    #ans.destroy()
    pass


def Enter1():

    for i in range(10):
        def Enter2():
            #global ans
            for i in range(10):

                #ans = Label(root, text= int(in1.get()) * i)
                #ans.pack_forget()
                #ans.pack()
                ansin = int(in1.get()) * i
                in2.insert(INSERT, ansin)



                Enter2()
        break
        #ans.destroy()
label = Label(
    root,
              text="Taable 2.0",

              font=44).pack()

test = Label(root, text="").pack()

test2 = Label(root, text="").pack()

test3 = Label(root, text="").pack()




label1 = Label(
    root,
               text="Enter The Times Table Number Below",
    font=44
    ).pack()

test4 = Label(root, text="").pack()

in1 = Entry(
    root,
    width=50
)
in1.get()
in1.pack()

btn = Button(root, text="ENTER..", command=Enter1).pack()
btn2 = Button(root, text="Delete Taable", command=DeleteTab)
btn2.pack()
in2 = Entry(root, width=50)
in2.pack(ipady=50)



root.mainloop()