from tkinter import *
parent=Tk()
parent.geometry("400x400")
name=Label(text="UserName").place(x=40,y=60)
password=Label(text="Password").place(x=40,y=90)
email=Label(text="Email").place(x=40,y=120)
nm=Entry().place(x=100,y=60)
password=Entry().place(x=100,y=90)
e=Entry().place(x=100,y=120)
login=Button(text="Login",fg='green').place(x=40,y=160)
cancel=Button(text='Cancel',fg='green').place(x=100,y=160)
parent.mainloop()