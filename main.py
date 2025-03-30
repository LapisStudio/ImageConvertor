import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox 

import random
from PIL import Image

def choose_file():
    file_path = filedialog.askopenfilename(title="Choose a file")
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path) 

def convert():
    file_path = entry_file.get()
    print(file_path)
    format_selected = format_combobox.get()
    if file_path and format_selected:
		
        with Image.open(file_path) as im:
            file = 'output'+str(random.randint(1,999))
            im.save(file + "." + format_selected.lower(), format=format_selected)
            
        messagebox.showinfo(title='Info', message="File: "+file_path)
        messagebox.showinfo(title='Info', message="Format to convert: "+file+'.'+format_selected)
    else:
        messagebox.showerror("Error", "Please, choice file and format!") 

root = tk.Tk()
root.title("Convertor Imeges")

label_file = tk.Label(root, text="Choice file:")
label_file.pack(pady=5)

entry_file = tk.Entry(root, width=50)
entry_file.pack(pady=5)

button_browse = tk.Button(root, text="Browse", command=choose_file)
button_browse.pack(pady=5)

label_format = tk.Label(root, text="Choice format:")
label_format.pack(pady=5)

formats = ["PNG", "JPG", "JPEG"]
format_combobox = ttk.Combobox(root, values=formats, width=20)
format_combobox.pack(pady=5)

button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack(pady=20)

root.mainloop()
