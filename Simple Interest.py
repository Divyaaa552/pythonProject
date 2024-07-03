from tkinter import *
window = Tk()
frame = Frame(window)
frame.place(x=700,y=100)

def calculate() :
    a = (int(PrincipleEntry.get() ) * int(TimeEntry.get() )* int(RateEntry.get() ) )/100
    AnswerLabel = Label(frame, text="Answer is :", font=('Arial', 15, 'bold'), bg='white',
                           fg='firebrick1')
    AnswerLabel.grid(row=5, column=0)
    aLabel = Label(frame, text= a, font=('Arial', 15, 'bold'), bg='white',
                           fg='firebrick1')
    aLabel.grid(row=5, column=1)

    print(a)
PrincipleLabel = Label(frame,text="Enter Principle Amount:",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
PrincipleLabel.grid(row=0,column=0)
PrincipleEntry = Entry(frame,width=30)
PrincipleEntry.grid(row=0,column=1)

TimeLabel = Label(frame,text="Enter Time:",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
TimeLabel.grid(row=1,column=0)
TimeEntry = Entry(frame,width=30)
TimeEntry.grid(row=1,column=1)

RateLabel = Label(frame,text="Enter Rate of Interest:",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
RateLabel.grid(row=2,column=0)
RateEntry = Entry(frame,width=30)
RateEntry.grid(row=2,column=1)

calculateButton = Button(frame,text="Calculate",command = calculate,font=('Arial',15,'bold'),bg='white',fg='firebrick1')
calculateButton.grid(row=4,column=1,)
frame.pack()
window.mainloop()