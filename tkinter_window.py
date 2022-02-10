from tkinter import *

import main
import record_audio


class TkInterWindow:
    def __init__(self):
        self.window = None
        self.back_btn = None

    def open_new_window(self, prev_win, title):
        prev_win.destroy()
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("800x500")

    def close_window(self):
        self.window.destroy()
