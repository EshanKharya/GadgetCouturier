import tkinter as tk
from tkinter import *
from tkinter import ttk
from plotter import store, read, desc, plot

def tablewin(choice, pmax, rmin):
    store(choice)
    database = read()
    twin = Tk()
    twin.geometry("1020x600")
    twin.configure(bg="#000099")
    twin.resizable(False, False)

    style = ttk.Style()
    style.configure("Treeview", background="#b3ffff", rowheight=25)
    style.map("Treeview", background=[('selected', 'green')])

    col = ("Title", "Price", "Stars", "Ratings", "Discount")
    tv = ttk.Treeview(twin, columns=col, show="headings", selectmode='browse')
    
    tv.heading(col[0], text="Title")
    tv.heading(col[1], text="Price")
    tv.heading(col[2], text="Stars")
    tv.heading(col[3], text="Ratings")
    tv.heading(col[4], text="Discount")

    for data in database:
        if float(data[1]) <= pmax and float(data[3]) >= rmin:
            tv.insert('', tk.END, values = tuple(data))

    titlelabel = Label(twin, text="Tabular Data", font=("Helvetica 20"), bg="#000099", fg="yellow").grid(row = 0, column = 0) 

    tv.grid(row=1, column=0, sticky="nsew")
    
    scrollbar = ttk.Scrollbar(twin, orient=tk.VERTICAL, command=tv.yview)
    tv.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

    extras = desc(pmax,rmin)
    subhead = Label(twin, text="Analysis", font=("Helvetica 16"), bg="#000099", fg="yellow").grid(row = 2, column = 0)
    extraslabel = Label(twin, text=extras, font=("Helvetica 14"), bg="#000099", fg="yellow").grid(row = 3, column = 0)

    plot(pmax, rmin)
    twin.mainloop()

