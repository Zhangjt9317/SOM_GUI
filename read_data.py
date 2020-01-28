# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *
from tkinter.ttk import *
import pickle
import pandas as pd
import pprint

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

root = Tk()
root.geometry('200x100')

# This function will be used to open
# file in read mode and only Python files
# will be opened
# def open_file():
#     file = askopenfilename(initialdir = "/",title = "Select file",filetypes =[("All files", "*.*")])
#     if file is not None:
#         # print(content)
#         content = open(file, "rb")
#         return pickle.load(content)

# ask to open csv file (csv file) with index of the first column


def open_file():
    file = askopenfilename(initialdir="/", title="Select Data", filetypes=[("csv files", "*.csv")])
    if file is not None:
        content = open(file, "rb")
        
        df = pd.read_csv(content)
        ind = df[df.columns[0]] # the first columns is zero
        df = df.set_index(ind)
        # print(df)
        return df

btn = Button(root, text='Open', command= lambda: open_file())
btn.pack(side=TOP, pady=10)

mainloop()
