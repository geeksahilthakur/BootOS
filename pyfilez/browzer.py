# Import tkinter and webview libraries
from tkinter import *
import webview

# define an instance of tkinter
tk = Tk()

#  size of the window where we show our website
tk.geometry("800x450")

# Open website
webview.create_window('Geek Sahil', 'https://anotherdimension.netlify.app/')
webview.start()