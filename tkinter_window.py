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
        self.window.resizable()

        self.back_btn = Button(self.window, text="Back to Homepage",
                               command=lambda: main.open_homepage_window(self.window))
        self.back_btn.grid(row=0, rowspan=1, column=0, columnspan=1)

        self.window.mainloop()

    def close_window(self):
        self.window.destroy()
