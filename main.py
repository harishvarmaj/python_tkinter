from tkinter import *

root=Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e58")
root.state("zoomed")
#Entries Frame
entries_frame = Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title = Label(entries_frame,text="Employee Management System",font=("Calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2)

lblName = Label(entries_frame,text="Name", font=("TimesNewRoman",14),bg="#535c68",fg="white")
lblName.grid(row=1,column=0)

root.mainloop()
