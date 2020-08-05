from tkinter import *
import calendar

root = Tk()
root.title("Calendar")

root.geometry("500x650")
Text=calendar.calendar(2020)

label1 = Label(root,text="CALENDAR",bg='dark gray',font=('arial',9,'bold'))
label1.grid(row=1,column=1)
root.config(background="white")
l1=Label(root,text = Text,font="Consoles 10")
l1.grid(row=2,column=1,padx=20)
root.mainloop()