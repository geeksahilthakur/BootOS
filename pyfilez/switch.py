import tkinter
import tkinter as tk
from tkinter import font as tkfont, messagebox

from pyfilez.tabs import tab2


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Frame(self, width=1500, height=788, bg="white").place(x=0, y=0)
        self.photo = tk.PhotoImage(file="smllogo.png")
        main_logo = tk.Label(self, image=self.photo, bg="white")
        main_logo.place(x=540, y=50)

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
                messagebox.showerror('Welcome to Boot OS', 'Welcome to Boot OS!')


            else:
                print("error")
                messagebox.showerror('Login Error', 'Error: incorrect credentials')

        kartik = tkinter.Label(text="Username", font=("", 14, ""), bg="white", fg="black").place(x=475, y=220)
        self.img_0 = tkinter.PhotoImage(file="rrr.png")
        r_entry = tkinter.Label(self, image=self.img_0, bg="white").place(x=470, y=255)
        user_name = tkinter.Entry(self, textvariable=name, width=30, bg="#D9D9D9", bd=0, font=("", 15, "")).place(x=485, y=266.5)

        kartik2 = tkinter.Label(text="Password", font=("", 14, ""), bg="white", fg="black").place(x=475, y=320)
        self.img_1 = tkinter.PhotoImage(file="rrr.png")
        r_entry_1 = tkinter.Label(self, image=self.img_1, bg="white").place(x=470, y=355)
        user_pass = tkinter.Entry(self, textvariable=password, width=30, bg="#D9D9D9", bd=0, font=("", 15, ""), show="*").place(
            x=485, y=366)

        self.photo_1 = tkinter.PhotoImage(file="lgnbtn.png")
        login_tn = tkinter.Button(self, image=self.photo_1, bg="white", fg="white", bd=0, command=hello)
        login_tn.place(x=470, y=450)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
