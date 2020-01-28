# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import *
from tkinter.ttk import *
import pickle 

# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry('200x100')

# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file(): 
    file = askopenfilename(initialdir = "/",title = "Select file",filetypes =[("All files", "*.*")]) 
    if file is not None:
        # print(content)
        content = open(file, "rb")
        return pickle.load(content)

btn = Button(root, text ='Open', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 

mainloop() 