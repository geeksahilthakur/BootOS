import tkinter
from tkinter import *
import time
from tkinter import messagebox

w = Tk()
w.geometry("1500x788")
w.title("Boot OS")
w.config(bg='white')

Frame(w, width=427, height=250, bg="white").place(x=0,y=0)
photo = PhotoImage(file="crplogo.png")
main_logo = Label(w, image=photo , bg="white")
main_logo.place(x=490 , y =171)

photo_a= PhotoImage(file="b.png")
photo_b= PhotoImage(file="y.png")


for i in range(3):
    l1=Label(w, image=photo_a ,border=0 ,relief=SUNKEN).place(x=590, y=390)
    l2=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=630, y=390)
    l3=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=670, y=390)
    l4=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=710, y=390)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=590, y=390)
    l2=Label(w, image=photo_a ,border=0 ,relief=SUNKEN).place(x=630, y=390)
    l3=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=670, y=390)
    l4=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=710, y=390)
    w.update_idletasks()
    time.sleep(0.5)


    l1=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=590, y=390)
    l2=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=630, y=390)
    l3=Label(w, image=photo_a ,border=0 ,relief=SUNKEN).place(x=670, y=390)
    l4=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=710, y=390)
    w.update_idletasks()
    time.sleep(0.5)


    l1=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=590, y=390)
    l2=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=630, y=390)
    l3=Label(w, image=photo_b ,border=0 ,relief=SUNKEN).place(x=670, y=390)
    l4=Label(w, image=photo_a ,border=0 ,relief=SUNKEN).place(x=710, y=390)
    w.update_idletasks()
    time.sleep(0.5)

w.destroy()


l = Tk()
l.geometry("1500x788")
l.title("Boot OS")
l.config(bg='white')
ic = PhotoImage(file = "wicn.ico")
l.iconphoto(False, ic)


Frame(l, width=427, height=250, bg="white").place(x=0,y=0)
photo = PhotoImage(file="smllogo.png")
main_logo = Label(l, image=photo , bg="white")
main_logo.place(x=540 , y =50)

name = tkinter.StringVar()
password = tkinter.StringVar()

def hello():
    name_1 = name.get()
    password_1 = password.get()

    print("Username: " + name_1)
    print("Password: " + password_1)

    uname = "Boot"
    pswd = "1234"

    if uname == name_1 and pswd == password_1:
        print("hello")
        messagebox.showerror('Welcome to Boot OS', 'Welcome to Boot OS!',icon='info')

    else:
        print("error")
        messagebox.showerror('Login Error', 'Error: incorrect credentials')

kartik = Label(text="Username",font=("",14,""),bg="white",fg="black").place(x=475,y=220)
img_0 = PhotoImage(file="rrr.png")
r_entry = Label(l, image=img_0, bg="white").place(x=470,y=255)
user_name = Entry(l,textvariable = name,width=30,bg="#D9D9D9", bd=0 ,font=("",15,"")).place(x=485,y=266.5)

kartik2 = Label(text="Password",font=("",14,""),bg="white",fg="black").place(x=475,y=320)
img_1 = PhotoImage(file="rrr.png")
r_entry_1 = Label(l, image=img_1, bg="white").place(x=470,y=355)
user_pass = Entry(l,textvariable = password,width=30,bg="#D9D9D9", bd=0 ,font=("",15,""),show="*").place(x=485,y=366)

photo_1 = PhotoImage(file="lgnbtn.png")
login_tn = Button(l, image=photo_1, bg="white",fg="white",bd=0,command=hello)
login_tn.place(x=470 , y =450)
l.mainloop()

w.mainloop()