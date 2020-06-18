import tkinter as tk
import pandas as pd


root = tk.Tk()


scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=1, sticky="NSw")

listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(tk.END,str(i))

listbox.grid(row=0, column=0, sticky="NSwE")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)

scrollbar.config(command=listbox.yview)

root.mainloop()