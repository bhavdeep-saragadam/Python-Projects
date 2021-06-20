from tkinter import *
from PIL import Image, ImageTk
import sqlite3
root = Tk()
root.title("QCloud Crystal")
root.geometry("800x600")
root.resizable(0,0)
root.iconbitmap('Icon.ico')
conn = sqlite3.connect('Database.db')

cur = conn.cursor()

conn.execute(''' CREATE TABLE data (tn text, tp text)''')

conn.commit()

conn.close()
my_img1 = ImageTk.PhotoImage(Image.open(r'Img1.png'))
my_img_label = Label(image=my_img1)
my_img_label.pack(ipadx=10)
label1 = Label(root, text="Team Name", fg="orange")
label1.pack()


tn = Entry(root, width=100)
tn.pack()
tn.get()

label2 = Label(root, text="Team Project", fg="orange")
label2.pack()

tp = Entry(root, width=100)
tp.pack()
tp.get()
file = open("Database.txt", "w")
def data():
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM Data")
    records = c.fetchall()
    print(records)

btn1 = Button(root, text="Add To Database", command=data)

btn1.pack()

root.mainloop()
