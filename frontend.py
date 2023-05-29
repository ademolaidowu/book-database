from tkinter import *
from tkinter import messagebox
import backend

def get_selected_row(event):
    try:
        global selection
        index = listbox.curselection()[0]
        selection = listbox.get(index)
        e1.delete(0, END)
        e1.insert(END, selection[1])
        e2.delete(0, END)
        e2.insert(END, selection[2])
        e3.delete(0, END)
        e3.insert(END, selection[3])
        e4.delete(0, END)
        e4.insert(END, selection[4])
    except IndexError:
        pass

def view_command():
    listbox.delete(0, END)
    for row in backend.viewall():
        listbox.insert(END, row)

def search_command():
    listbox.delete(0, END)
    for row in backend.search(title_entry.get(), author_entry.get(), isbn_entry.get(), year_entry.get()):
        listbox.insert(END, row)

def addentry_command():
    backend.insert(title_entry.get(), author_entry.get(), isbn_entry.get(), year_entry.get())
    listbox.delete(0, END)
    listbox.insert(END,(title_entry.get(), author_entry.get(), isbn_entry.get(), year_entry.get()))
    view_command()

def delete_command():
    backend.delete(selection[0])
    view_command()

def update_command():
    backend.update(selection[0], title_entry.get(), author_entry.get(), isbn_entry.get(), year_entry.get())
    listbox.delete(0, END)
    listbox.insert(END, (title_entry.get(), author_entry.get(), isbn_entry.get(), year_entry.get()))
    view_command()

def close_command():
    close = messagebox.askyesno("Close dialog", "Do you want to exit Book Database")
    if close:
        import sys; sys.exit()
    else:
        return None


root = Tk()
root.title("Book Database")
# root.iconbitmap("book.ico")

"""LABELS"""
l1 = Label(root, text="Title")
l1.grid(row=0, column=0)

l2 = Label(root, text="Author")
l2.grid(row=1, column=0)

l3 = Label(root, text="ISBN")
l3.grid(row=2, column=0)

l4 = Label(root, text="Year")
l4.grid(row=2, column=2)


"""ENTRY"""
title_entry = StringVar()
e1 = Entry(root, textvariable=title_entry, width=45)
e1.grid(row=0, column=1, columnspan=4)

author_entry = StringVar()
e2 = Entry(root, textvariable=author_entry, width=45)
e2.grid(row=1, column=1, columnspan=4)

isbn_entry = StringVar()
e3 = Entry(root, textvariable=isbn_entry)
e3.grid(row=2, column=1)

year_entry = StringVar()
e4= Entry(root, textvariable=year_entry, width=15)
e4.grid(row=2, column=3)

"""LIST BOX"""
listbox = Listbox(root, height=10, width=35)
listbox.grid(row=3, column=0, rowspan=8, columnspan=2)

sb = Scrollbar(root)
sb.grid(row=3, column=2, rowspan=7)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

listbox.bind("<<ListboxSelect>>", get_selected_row)


"""BUTTONS"""
b1 = Button(root, text="View all", width=12, command=view_command)
b1.grid(row=3, column=3)

b2 = Button(root, text="Search entry", width=12, command=search_command)
b2.grid(row=4, column=3)

b3 = Button(root, text="Add Entry", width=12, command=addentry_command)
b3.grid(row=5, column=3)

b4 = Button(root, text="Update", width=12, command=update_command)
b4.grid(row=6, column=3)

b5 = Button(root, text="Delete", width=12, command=delete_command)
b5.grid(row=7, column=3)

b6 = Button(root, text="Close", width=12, command=close_command)
b6.grid(row=8, column=3)

root.mainloop()