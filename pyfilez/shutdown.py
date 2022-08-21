import tkinter
from tkinter import *
import time



shut_down = Tk()
shut_down.geometry("1500x788")
shut_down.title("Boot OS")
shut_down.config(bg='white')
ic = PhotoImage(file = "wicn.ico")
shut_down.iconphoto(False, ic)
shut_down.overrideredirect(1)


Frame(shut_down, width=1500, height=788, bg="white").place(x=0,y=0)
photo = PhotoImage(file="crplogo.png")
main_logo = Label(shut_down, image=photo , bg="white")
main_logo.place(x=450 , y =171)

photo_a= PhotoImage(file="b.png")
photo_b= PhotoImage(file="y.png")

shutdown_text = Label(shut_down,text="Shutting down...", font=("", 14, ""), bg="white", fg="black").place(x=580, y=600)

for i in range(2):
    l1=Label(shut_down, image=photo_b ,border=0 ,relief=SUNKEN).place(x=600, y=435)#left
    l2=Label(shut_down, image=photo_a ,border=0 ,relief=SUNKEN).place(x=638, y=400) #top
    l3=Label(shut_down, image=photo_b ,border=0 ,relief=SUNKEN).place(x=675, y=435) #right
    l4=Label(shut_down, image=photo_b ,border=0 ,relief=SUNKEN).place(x=665, y=410) #rightup
    l5 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=460) #rightdown
    l6=Label(shut_down, image=photo_b ,border=0 ,relief=SUNKEN).place(x=638, y=470) #bottom
    l7 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop
    l8 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=460) #leftbottom
    shut_down.update_idletasks()
    time.sleep(0.5)

    l1 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=600, y=435)  # left
    l2 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=400)  # top
    l4 = Label(shut_down, image=photo_a, border=0, relief=SUNKEN).place(x=665, y=410)  # rightup
    l3 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=675, y=435)  # right
    l5 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=460)  # rightdown
    l6 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=470)  # bottom
    l8 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=460)  # leftbottom
    l7 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop

    shut_down.update_idletasks()
    time.sleep(0.5)

    l1 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=600, y=435)  # left
    l2 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=400)  # top
    l4 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=410)  # rightup
    l3 = Label(shut_down, image=photo_a, border=0, relief=SUNKEN).place(x=675, y=435)  # right
    l5 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=460)  # rightdown
    l6 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=470)  # bottom
    l8 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=460)  # leftbottom
    l7 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop

    shut_down.update_idletasks()
    time.sleep(0.5)

    l1 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=600, y=435)  # left
    l2 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=400)  # top
    l4 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=410)  # rightup
    l3 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=675, y=435)  # right
    l5 = Label(shut_down, image=photo_a, border=0, relief=SUNKEN).place(x=665, y=460)  # rightdown
    l6 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=470)  # bottom
    l8 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=460)  # leftbottom
    l7 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop

    shut_down.update_idletasks()
    time.sleep(0.5)

    l1 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=600, y=435)  # left
    l2 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=400)  # top
    l4 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=410)  # rightup
    l3 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=675, y=435)  # right
    l5 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=460)  # rightdown
    l6 = Label(shut_down, image=photo_a, border=0, relief=SUNKEN).place(x=638, y=470)  # bottom
    l8 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=460)  # leftbottom
    l7 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop

    shut_down.update_idletasks()
    time.sleep(0.5)

    l2 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=400)  # top
    l4 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=410)  # rightup
    l3 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=675, y=435)  # right
    l5 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=460)  # rightdown
    l6 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=470)  # bottom
    l8 = Label(shut_down, image=photo_a, border=0, relief=SUNKEN).place(x=610, y=460)  # leftbottom
    l1 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=600, y=435)  # left
    l7 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop

    shut_down.update_idletasks()
    time.sleep(0.5)

    l2 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=400)  # top
    l4 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=410)  # rightup
    l3 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=675, y=435)  # right
    l5 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=460)  # rightdown
    l6 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=470)  # bottom
    l8 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=460)  # leftbottom
    l1 = Label(shut_down, image=photo_a, border=0, relief=SUNKEN).place(x=600, y=435)  # left
    l7 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop

    shut_down.update_idletasks()
    time.sleep(0.5)

    l2 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=400)  # top
    l4 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=410)  # rightup
    l3 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=675, y=435)  # right
    l5 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=460)  # rightdown
    l6 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=470)  # bottom
    l8 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=460)  # leftbottom
    l1 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=600, y=435)  # left
    l7 = Label(shut_down, image=photo_a, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop

    shut_down.update_idletasks()
    time.sleep(0.5)

    l2 = Label(shut_down, image=photo_a, border=0, relief=SUNKEN).place(x=638, y=400)  # top
    l4 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=410)  # rightup
    l3 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=675, y=435)  # right
    l5 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=665, y=460)  # rightdown
    l6 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=638, y=470)  # bottom
    l8 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=460)  # leftbottom
    l1 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=600, y=435)  # left
    l7 = Label(shut_down, image=photo_b, border=0, relief=SUNKEN).place(x=610, y=410)  # lefttop

    shut_down.update_idletasks()
    time.sleep(0.5)


shut_down.destroy()
