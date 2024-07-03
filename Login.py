from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
def saveData() :
    try:
         conn = mysql.connector.connect(
                   host='localhost',
                    user='root',
                   password='Sindhuri1@',
                   database='userdata'
            )
    except:
            messagebox.showerror('Error','Problem in database connection')
    if(usernameEntry.get()=='' or emailEntry.get()=='' or passwordEntry.get()==''):
        messagebox.showerror('Error',"All fields are mandatory")
    else :
         mycursor = conn.cursor()
         sql='insert into student(username,email,password)values(%s,%s,%s);'
         #mycursor.execute(sql,(usernameEntry.get(),emailEntry.get(),passwordEntry.get()))
         data = (usernameEntry.get(), emailEntry.get(), passwordEntry.get())
         mycursor.execute(sql,data)
         conn.commit()
         messagebox.showinfo('Success',"Data saved successfully")

    if(conn):
        print("Success")
      #messagebox.showinfo("Success")

    else :
       print("Problem in Database Connection")
       #messagebox.showerror("Problem in database")
window=Tk()
background=ImageTk.PhotoImage(file="moon.jpg")
blabel=Label(window,image=background)
blabel.grid()
frame=Frame(window)
frame.place(x=600,y=100)
usernameLabel=Label(frame,text="Username",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=0,column=0)
usernameEntry=Entry(frame,width=20)
usernameEntry.grid(row=0,column=1)
emailLabel=Label(frame,text="E-mail",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0)
emailEntry=Entry(frame,width=20)
emailEntry.grid(row=1,column=1)
passwordLabel=Label(frame,text="Password",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=2,column=0)
passwordEntry=Entry(frame,width=20)
passwordEntry.grid(row=2,column=1)
button=Button(frame,text="Save",command=saveData)
button.grid(row=3,column=1)


window.mainloop()
