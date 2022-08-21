import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from self import self



window = Tk()
window.geometry("1500x788")
window.overrideredirect(1)
notebook = ttk.Notebook(window)

tab1 = Frame(notebook, bg="white")

tab2 = Frame(notebook, bg="white")

notebook.add(tab1, text=" ⌂ ")
notebook.add(tab2, text="Recent Apps")
notebook.pack(expand=True, fill="both")

# tab1 starts
sm_logo = PhotoImage(file="minilogo.png")
main_logo = Label(tab1, image=sm_logo, bg="white")
main_logo.place(x=30, y=20)

search_png = PhotoImage(file="serchbar.png")
search_bar = Label(tab1, image=search_png, bg="white")
search_bar.place(x=300, y=25)

search_txt = Entry(tab1, width=90, bg="white", bd=0, font=("", 10, "")).place(x=312, y=31)

def sht():
    messagebox.showerror('Boot OS', 'You are about to shutdown Boot OS!', icon='info')
    window.destroy()
    import shutdown

off_png = PhotoImage(file="off.png")
off_btn = Button(tab1, image=off_png, bg="white", bd=0, command=sht)
off_btn.place(x=1200, y=25)
# tab1end

Label(tab2, text="Recent Apps:", bg="white").place(x=590, y=20)
##################################################################################################################
a = [0]
def add_tab():
    if a == [0]:
        v = 1
        a.append(v)
        tab3 = Frame(notebook, bg="white")
        notebook.add(tab3, text="Browser")
        Frame(tab3, width=427, height=250, bg="white").place(x=0, y=0)
        self.photo = tkinter.PhotoImage(file='11.png')
        self.main_logo = Label(tab3, image=self.photo, bg="white")
        self.main_logo.place(x=540, y=50)

        def sw():
            notebook.select(tab3)
        self.icon = tkinter.PhotoImage(file='1.png')
        self.main_logo = Button(tab2, image=self.icon, bg="white", bd=0, command=sw)
        self.main_logo.place(x=540, y=100)

        def back():
            tab3.destroy()
            self.main_logo.destroy()
            a.remove(v)
            notebook.select(tab1)
            print("back", a)

        exit_button = Button(tab3, text="Exit", command=back).place(x=610,y=10)
        print("bngyi window ")
        print(a)
        notebook.select(tab3)

    else:
        messagebox.showerror('Boot OS', 'App already opend ', icon='info')
        notebook.select(tab2)


###################################################################################################################

# btn = Button(tab1, text='Add new tab', bd='0', command=add_tab, width=20)
# btn.place(x=550, y=450)

bg_img = PhotoImage(file='yellow.png')
bgg = Label(tab1, image=bg_img , bg="white",fg="white")
bgg.place(x=180, y =90)

app = Label(tab1, text="All Apps",font=("",15,"") ,bg="#FAB80A").place(x=610 ,y =130)
####

bsr_img = PhotoImage(file='1.png')
bsr = Button(tab1, image=bsr_img,bg="#FAB80A",bd="0",command=add_tab).place(x=255, y=200)

notez_img = PhotoImage(file='2.png')
notez = Button(tab1, image=notez_img,bg="#FAB80A",bd="0").place(x=560,y=200)

gamez_img = PhotoImage(file='3.png')
gamez = Button(tab1, image=gamez_img,bg="#FAB80A",bd="0").place(x=860,y=200)

####
muz_img = PhotoImage(file='4.png')
muz = Button(tab1, image=muz_img,bg="#FAB80A",bd="0").place(x=255,y=400)

set_img = PhotoImage(file='5.png')
set = Button(tab1, image=set_img,bg="#FAB80A",bd="0").place(x=560,y=400)

as_img = PhotoImage(file='6.png')
abuts = Button(tab1, image=as_img,bg="#FAB80A",bd="0").place(x=860,y=400)




window.mainloop()



