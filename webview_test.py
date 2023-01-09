# import required library
from tkinter import *
import webview

# define an instance of tkinter
tk = Tk()


# Open website
webview.create_window('poop in a box', 'https://ericpolley.com')
webview.start()
