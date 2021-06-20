from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("DeepTxt")
root.geometry("1200x660")

def new_file():
    my_text.delete("1.0", END)
    root.title("New DeepTxt")
    status_bar.config(text="New File        ")

def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfile(initialdir=r"C:\Users\esbha" , title="Open File", filetypes=(("Text Files",

                                                                                            "*.txt"),
                                                                                           ("All Files",
                                                                                            "*.*")))
    name = text_file
    status_bar.config(text=f'{name}             ')
    name = my_text.replace("1.0",r"C:\Users\esbha", "")
    root.title(f'{name} - DeepTxt!')

    text_file = open(text_file, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)

        

my_frame = Frame(root)
my_frame.pack(pady=5)
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16),
               selectbackground="blue", selectforeground="white",
               undo=True,
               yscrollcommand=text_scroll.set)
my_text.pack()
text_scroll.config(command=my_text.yview)

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()