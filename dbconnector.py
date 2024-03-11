from tkinter import *
import mysql.connector

window = Tk()
frame = Frame(window)
frame.place(x=700,y=100)
frame.pack()
window.mainloop()
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deepu@25"
)
mycur=conn.cursor()
if(mycur) :
    print("Success")
else :
    print("Problem in database")

q = "use customerdata"
mycur.execute(q)
#query = "create table studentdb(name varchar(100),rollno varchar(100))"
#mycur.execute(query)
#p = "drop table studentdb"
#mycur.execute(p)