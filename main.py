# Youtube Video Dowloader
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("800x300")
root.title("NebulaTech : Youtube Video Downloader : YVD")


def download():
    url = YouTube(str(userin.get()))
    video = url.streams.first()
    video.download()
    userin.delete(0, END)


txt1 = Label(root, text="Paste Youtube URL here: ")
txt1.config(font=(44))
txt1.pack()

test2 = Label(root, text="")
test2.pack()

test3 = Label(root, text="")
test3.pack()

test4 = Label(root, text="")
test4.pack()

test5 = Label(root, text="")
test5.pack()

link = StringVar

userin = Entry(root, width=50, textvariable=link)
userin.pack()

test6 = Label(root, text="")
test6.pack()

test7 = Label(root, text="")
test7.pack()

test8 = Label(root, text="")
test8.pack()

btn1 = Button(root, text="DOWNLOAD", command=download)
btn1.pack(ipadx=30, ipady=25)

root.mainloop()
