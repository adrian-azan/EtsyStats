import tkinter as tk
import pandas as pd
import tutor as tut

root = tk.Tk()
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=1, sticky="NSw")
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, font=18)
listbox.grid(row=0, column=0, sticky="NSwE")
scrollbar.config(command=listbox.yview)


info = tk.Frame(root)
info2 = tk.Label(info,bg="green")

info.grid(row=0,column=2,sticky="NSWE")
info2.pack(expand=True, fill="both")

root.columnconfigure(2,weight=5)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=0)
root.rowconfigure(0,weight=1)




#----------READING FILE

mySelf = tut.tutor()
test = pd.read_excel("lessons.xlsx")

for value in test.values:    
    student = mySelf.addStudent(value[4],value[5])
    if student:
        mySelf.addLesson(student, value)
    #print(value[0].split("\n"))
    
mySelf.students.sort()
mySelf.printLessons()


for i in mySelf.students:
    listbox.insert(tk.END,(i.name + " (" + i.subject + ")"))







root.mainloop()