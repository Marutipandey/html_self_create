from tkinter import Tk,Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox
from mysql_config import  dbConfig
import mysql.connector as pyo


con=pyo.connect(**dbConfig)
cursor=con.cursor()

class Bookdb:
    def __init__(self):
        self.con=pyo.connect(**dbConfig)
        self.cursor=con.cursor()
        print("You have connected to the database")
        print(con)

def __del__(self):
    self.con.close()

def view(self):
    self.cursor.execute("SELECT*FROM books")
    rows=self.cursor.fetchall()
    return rows

def insert(self,title,auther,isbn):
    sql=("INSERT books(title,auther,isbn)VALUES(%s,%s,%s)")
    values=[title,auther,isbn]
    self.cursor.execute(sql,values)
    self.con.commit()
    messagebox.showinfo(title="Book Database",message="New book added to database")

def update(self,id,title,auther,isbn):
    tsql='UPDATE books SET title=%s,auther=%s,isbn=%s WHERE id=%s'
    self.cursor.execute(tsql,[title,auther,isbn,id])
    self.con.commit()
    messagebox.showinfo(title="Bool Database",message="Book Updated")
