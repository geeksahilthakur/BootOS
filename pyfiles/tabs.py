import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from self import self

window = Tk()
window.geometry("1500x788")

notebook = ttk.Notebook(window)

tab1 = Frame(notebook,bg="white")

tab2 = Frame(notebook,bg="white")

notebook.add(tab1,text="Home")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both")
Label(tab1,text="Hello, this is tab#1",width=50,height=25,bg="white").pack()
Label(tab2,text="Goodbye, this is tab#2",width=50,height=25 ,bg="white").pack()

exit_button = Button(tab2, text="Exit", command=tab2.destroy)
exit_button.pack(pady=20)

###########################################
a = [0]
def add_tab():
    if a == [0]:
        tab3 = Frame(notebook, bg="white")
        notebook.add(tab3, text="Tab 3")
        Label(tab3, text="First app", bg="white").pack()
        Frame(tab3, width=427, height=250, bg="white").place(x=0, y=0)
        self.photo = tkinter.PhotoImage(file='smllogo.png')
        main_logo = Label(tab3, image=self.photo, bg="white")
        main_logo.place(x=540, y=50)
        notebook.select(tab3)
        print("bngyi window ")
        v = 1
        a.append(v)
        print(a)
    else:
        messagebox.showerror('Boot OS', 'App already opend ', icon='info')

##############################################

btn = Button(tab1, text = 'Add new tab', bd = '5',command =add_tab, width=20)
btn.place(x=550 , y =450)

window.mainloop()