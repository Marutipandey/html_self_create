import  tkinter
from tkinter import ttk, W, E
from tkinter import messagebox


root = tkinter.Tk();



root.title("my books database application")


root.configure(background="light green")
root.geometry('800x900')
root.resizable(width=False,height=False)



title_label=ttk.Label(root,text='Title' ,background='light green',font=('TkDefaultFont',16))
title_label.grid(row=0,column=0,sticky=W)
title_text= tkinter.StringVar()
title_entry=ttk.Entry(root,width=24,textvariable=title_text)
title_entry.grid(row=0,column=1,sticky=W)


title_label=ttk.Label(root,text='Auther' ,background='light green',font=('TkDefaultFont',16))
title_label.grid(row=0,column=2,sticky=W)
title_text= tkinter.StringVar()
title_entry=ttk.Entry(root,width=24,textvariable=title_text)
title_entry.grid(row=0,column=3,sticky=W)


title_label=ttk.Label(root,text='ISBN' ,background='light green',font=('TkDefaultFont',16))
title_label.grid(row=0,column=4,sticky=W)
title_text= tkinter.StringVar()
title_entry=ttk.Entry(root,width=24,textvariable=title_text)
title_entry.grid(row=0,column=5,sticky=W)

add_btn= tkinter.Button(root, text="add book", bg='blue', fg='white', font='helvatica 10 bold',command="")
add_btn.grid(row=0,column=6,sticky=W)

list_bx= tkinter.Listbox(root, height=16, width=40, font="helvatica 13", bg="light blue")
list_bx.grid(row=3,column=1,columnspan=14,sticky=W+E,pady=40,padx=15)

modify_btn= tkinter.Button(root, text="add book", bg='blue', fg='white', font='helvatica 10 bold',command="")
modify_btn.grid(row=20,column=4)

view_btn= tkinter.Button(root, text="view all record", bg='blue', fg='white', font='helvatica 10 bold',command="")
view_btn.grid(row=15,column=5)

delete_btn= tkinter.Button(root, text="delete record", bg='blue', fg='white', font='helvatica 10 bold',command="")
delete_btn.grid(row=15,column=1)

exit_btn= tkinter.Button(root, text="exit", bg='blue', fg='white', font='helvatica 10 bold',command="")
exit_btn.grid(row=15,column=2)

clear_btn= tkinter.Button(root, text="clear screen", bg='blue', fg='white', font='helvatica 10 bold',command="")
clear_btn.grid(row=15,column=3)


root.mainloop()