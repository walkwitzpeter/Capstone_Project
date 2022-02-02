from playsound import playsound
from tkinter import *

import tkinter_window

# TODO possibilities
'''
Get list of highest probability words from Google API
'''

# Ideas for "game modes"
'''
Type say see - user types the word (from a picture) then says the word (after they typed it right) then sees the word 
Basic association - sees a photo says the word (start with this?)

'''


def play_audio():
    playsound(r'C:\Users\Peter Walkwitz\PyCharm_Capstone\MySpeechTherapy\test_recording.wav')


def open_homepage_window(prev_win=None):
    if prev_win is not None:
        prev_win.destroy()
    # TODO add method for destroying prev win
    window = Tk()
    window.title('Speaking with Peter Rabbit')
    window.geometry("800x500")
    window.resizable()
    img = PhotoImage(file="Homepage Image.png")
    label = Label(
        window,
        image=img,
        height=window.winfo_screenheight(),
        width=window.winfo_screenwidth()
    )
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Making my different activity buttons
    associations_btn = Button(window, text="Basic Associations", command=lambda: open_basic_association(window))
    type_say_see_btn = Button(window, text="Type, Say, See", command=lambda: open_type_say_see(window))

    # Putting them on the screen and configuring the Grid
    associations_btn.grid(row=0, rowspan=2, column=0, columnspan=2)
    type_say_see_btn.grid(row=1, rowspan=2, column=0, columnspan=2)

    # Making my buttons to record audio
    # exit_button = Button(window, text="Exit", command=lambda: window.destroy())
    # record_audio_btn = Button(window, text="Start Recording", command=lambda: record_audio.RecAUD())
    # see_audio_text_btn = Button(window, text="See Audio Text", command=lambda: google_api.GoogleAPI().get_transcript())
    # play_audio_btn = Button(window, text="Play Audio", command=lambda: play_audio())
    #
    # # Putting my buttons on the screen, and configuring the Grid
    # record_audio_btn.grid(row=0, rowspan=2, column=0, columnspan=2)
    # exit_button.grid(row=2, rowspan=2, column=1, columnspan=2)
    # see_audio_text_btn.grid(row=0, rowspan=1, column=3, columnspan=2)
    # play_audio_btn.grid(row=1, rowspan=1, column=3, columnspan=2)
    #
    # # Organizing the grid for my button layout
    for row_number in range(3):
        Grid.rowconfigure(window, row_number, weight=1)
    # for column_number in range(4):
    #     Grid.columnconfigure(window, column_number, weight=1)

    window.mainloop()


def open_basic_association(prev_win):
    tk = tkinter_window.TkInterWindow()
    tk.open_new_window(prev_win, "Basic Associations")
    main = tk.window
    # main = Toplevel()
    # main.resizable()

    #TODO
    # create label to hold photo
    # create record button
    # create see word button
    # create hear recording button
    img = PhotoImage(file="Homepage Image.png", master=main)
    label = Label(
        main,
        image=img,
        height=main.winfo_screenheight(),
        width=main.winfo_screenwidth()
    )
    label.place(x=0, y=0, relwidth=1, relheight=1)


def open_type_say_see(prev_win):
    tk = tkinter_window.TkInterWindow()
    tk.open_new_window(prev_win, "Type Say See Hear")


if __name__ == '__main__':
    open_homepage_window()

# Sources (description below the links)
# https://realpython.com/playing-and-recording-sound-python/#recording-audio
#     Used for how to record and playback audio
# https://www.daniweb.com/programming/software-development/threads/426702/problem-in-music-player
#     Used to fix my error when trying to play the sound
# https://www.youtube.com/watch?v=NytF3pJSMc8&ab_channel=Codemy.com
#     Used for TKinter basics (And other Codemy.com videos on youtube)
# https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
# https://twitter.com/humanbrainproj/status/1233727365768974336?lang=eu
#     Used for images
# https://www.iconsdb.com/blue-icons/microphone-icon.html
#     Used for my microphone image
# https://stackoverflow.com/questions/30786337/tkinter-windows-how-to-view-window-in-windows-task-bar-which-has-no-title-bar/30819099#30819099
#     Used to get rid of titlebar
# https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
#     Used to move my window to open at a certain location
# https://stackoverflow.com/questions/58764064/importerror-cannot-import-name-speech-from-google-cloud-unknown-location
# https://stackoverflow.com/questions/36183486/importerror-no-module-named-google
# https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm
# https://www.hellocodeclub.com/python-speech-recognition-create-program-with-google-api/
#     Getting my API to work
# https://stackoverflow.com/questions/10158552/how-to-use-an-image-for-the-background-in-tkinter
#     Using an image as background
# https://stackoverflow.com/questions/6434482/python-function-overloading
#     Defining a function with a "none" input
