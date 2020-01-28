import tkinter as tk
from tkinter import ttk

def callbackFunc(event):
     print(comboExample.get())
     
app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose the method")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=["var","mean","else"])


comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)
app.mainloop()