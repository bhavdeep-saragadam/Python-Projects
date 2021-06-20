#Database
from tkinter import *
import sqlite3
root = Tk()
root.title("Address Book")
root.geometry("400x400")
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

#c.execute("""
   # CREATE TABLE addresses (
    #f_name text,
    #l_name text,
    #city text,
    #state text,
    #zipcode integer)
#""")

def submit():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    c.execute('INSERT INTO addresses VALUES )(f_name, l_name, city, state, address, zip_code))',
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'address': address.get(),
                  'zip_code': zip_code.get()
              })
    conn.commit()

    conn.close()

def query():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    for record in records:
        records += str(record) +"\n"
    query_label = Label(root, text=records)
    query_label.grid(row=8, column=0, columnspan=2)
    print(records)
    conn.commit()
    conn.close()
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=2, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=3, column=1, padx=20)
zip_code = Entry(root, width=30)
zip_code.grid(row=4, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=5, column=1, padx=20)

f_label = Label(root, text="First Name")
f_label.grid(row=0, column=0)
l_label = Label(root, text="Last Name")
l_label.grid(row=1, column=0)
ad_label = Label(root, text="Address")
ad_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
z_label = Label(root, text="Zip")
z_label.grid(row=5, column=0)

sub_btn = Button(root, text="Submit", command=submit)
sub_btn.grid(row=6,column=0, columnspan=2, pady=10, padx=10, ipadx=100)

q_btn = Button(root, text="Show Records", command=query)
q_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
conn.commit()

conn.close()


root.mainloop()