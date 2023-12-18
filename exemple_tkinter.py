from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

def quit_application():
    root.quit()

quit_button = ttk.Button(frm, text="Quitter", command=quit_application)
quit_button.grid(column=0, row=1)


root.mainloop()