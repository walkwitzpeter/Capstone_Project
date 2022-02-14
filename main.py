import tkinter
from queue import LifoQueue

from playsound import playsound
from tkinter import *

import google_api
import record_audio
import tkinter_window

# TODO possibilities
import word_image_dictionary

'''
Get list of highest probability words from Google API
'''

# Ideas for "game modes"
'''
Type say see - user types the word (from a picture) then says the word (after they typed it right) then sees the word 
Basic association - sees a photo says the word (start with this?)

'''


def open_homepage_window(prev_win=None):
    if prev_win is not None:
        prev_win.destroy()
    window = Tk()
    window.title('Speaking with Peter Rabbit')
    window.geometry("800x500")
    img = PhotoImage(file="Photos/Homepage Image.png")
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
    # Grid size variables
    COLUMNS = 8
    ROWS = 8
    # Tk variables
    tk = tkinter_window.TkInterWindow()
    tk.open_new_window(prev_win, "Basic Associations")
    main = tk.window
    # Loading right answer and wrong answer pictures
    red_x = PhotoImage(file="Photos/Red X.png").subsample(9, 9)
    green_check = PhotoImage(file="Photos/Green Check.png").subsample(9, 9)

    # Creating something to keep track of what the current answer is and load photos
    photos_and_answers = word_image_dictionary.Words()
    photos_and_answers.initializeStacks()

    # Making my grid to place items
    for row_number in range(ROWS):
        Grid.rowconfigure(main, row_number, weight=2)
    for column_number in range(COLUMNS):
        Grid.columnconfigure(main, column_number, weight=2)

    # Setting up the first image/answer for the user
    img = photos_and_answers.imgStack.pop()
    photos_and_answers.updateCurAnswer()
    main_img = Label(main, image=img)
    main_img.grid(row=1, rowspan=2, column=3, columnspan=3)

    # Setting up the record button for the user
    record_audio_btn = Button(main, text="Record Answer", command=lambda: record_audio.RecAUD())
    record_audio_btn.grid(row=4, column=4)
    # Seeing the recording text
    recording_text = Label(main, text="Your answer appears here", compound=LEFT)
    recording_text.grid(row=5, column=4, columnspan=2)
    check_recording_btn = Button(main, text="Check Recording",
                                 command=lambda: check_recording(recording_text, photos_and_answers.curAnswer,
                                                                 green_check, red_x))
    check_recording_btn.grid(row=4, column=5)
    # Hiding the check recording button until user records something
    # check_recording_btn.grid_remove()

    # Placing my back and next arrows
    back_arw_img = tkinter.PhotoImage(master=main, file=r"Photos/Back Arrow.png").subsample(7, 7)
    back_btn = Button(main, text="Back", command=lambda: open_homepage_window(main), image=back_arw_img)
    back_btn.grid(row=0, column=0)
    next_arw_img = tkinter.PhotoImage(master=main, file=r"Photos/Next Arrow.png").subsample(9, 9)
    next_arw_btn = Button(main, text="Next",
                          command=lambda: update_image(main_img, photos_and_answers.imgStack, photos_and_answers,
                                                       recording_text),
                          image=next_arw_img)
    next_arw_btn.grid(row=ROWS, column=COLUMNS)

    # Assigning back/next button rows and columns to be smaller than the rest
    Grid.rowconfigure(main, 0, weight=1)
    Grid.columnconfigure(main, 0, weight=1)
    Grid.rowconfigure(main, ROWS, weight=1)
    Grid.columnconfigure(main, COLUMNS, weight=1)

    main.mainloop()


def open_type_say_see(prev_win):
    # Grid size variables
    COLUMNS = 8
    ROWS = 8
    # Tk Variables
    tk = tkinter_window.TkInterWindow()
    tk.open_new_window(prev_win, "Type Say See Hear")
    main = tk.window
    # Setting up answer images
    red_x = PhotoImage(file="Photos/Red X.png").subsample(9, 9)
    green_check = PhotoImage(file="Photos/Green Check.png").subsample(9, 9)

    img = tkinter.PhotoImage(file="Photos/mic_image.png", master=main)
    label = Label(
        main,
        image=img,
        height=main.winfo_screenheight(),
        width=main.winfo_screenwidth()
    )
    label.place(x=0, y=0, relwidth=1, relheight=1)

    back_btn = Button(main, text="Back to Homepage", command=lambda: open_homepage_window(main))
    back_btn.grid(row=0, rowspan=1, column=0, columnspan=1)


def check_recording(recording_text, cur_answer, check, red_x):
    if cur_answer != "Done":
        text = str(google_api.GoogleAPI().get_transcript())
        recording_text['text'] = "We heard the following possibilities:\n" + text
        recording_text.grid()
        print("cur_answer: " + cur_answer)
        if text.casefold().__contains__(cur_answer.casefold()):
            recording_text['image'] = check
            print("found")
        else:
            recording_text['image'] = red_x
            print("not found")
    else:
        recording_text['text'] = "You went through all the words!"
        recording_text.grid()


def update_image(label, img_stack, photos_and_answers, recording_text):
    # Changing image if there is another image waiting and update answer
    if img_stack:
        img = img_stack.pop()
        label.configure(image=img)
        label.image = img
        photos_and_answers.updateCurAnswer()
        recording_text.grid_remove()


if __name__ == '__main__':
    open_homepage_window()

# Sources (description below the links)
# https://realpython.com/playing-and-recording-sound-python/#recording-audio
#     Used for how to record and playback audio
# https://www.daniweb.com/programming/software-development/threads/426702/problem-in-music-player
#     Used to fix my error when trying to play the sound
# https://www.youtube.com/watch?v=NytF3pJSMc8&ab_channel=Codemy.com
# https://pythonprogramming.altervista.org/python-gui-with-tkinter-labels-with-text-and-images/?doing_wp_cron=1644523669.3052639961242675781250
# https://www.delftstack.com/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/#grid-remove-method-to-hide-tkinter-widgets-if-grid-layout-is-used
#     Used for TKinter basics (And other Codemy.com videos on youtube)
# https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
# https://twitter.com/humanbrainproj/status/1233727365768974336?lang=eu
# https://www.iconfinder.com/icons/329731/back_arrow_left_previous_return_icon
# https://commons.wikimedia.org/wiki/File:Apple_icon_1.png
# https://www.pngwing.com/en/free-png-kqaob
# https://www.iconsdb.com/green-icons/check-mark-3-icon.html
# https://www.dictionary.com/e/emoji/cross-mark-emoji/
# https://shop.passionfoods.com.au/search?q%5B%5D=category%3Awheat&sort_by=discount_percent
# https://www.ebay.com/itm/303883647178
# https://houseofhealthcollective.com.au/category/dried-fruit-nuts
# https://www.pinterest.com/pin/free-orange-radio-2-icon-download-orange-radio-2-icon--613404411743203644/
# https://www.crunchbase.com/organization/done-38e9
# https://www.iconsdb.com/blue-icons/microphone-icon.html
# https://stackoverflow.com/questions/10158552/how-to-use-an-image-for-the-background-in-tkinter
#     Used for images
# https://stackoverflow.com/questions/30786337/tkinter-windows-how-to-view-window-in-windows-task-bar-which-has-no-title-bar/30819099#30819099
#     Used to get rid of titlebar
# https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
#     Used to move my window to open at a certain location
# https://stackoverflow.com/questions/58764064/importerror-cannot-import-name-speech-from-google-cloud-unknown-location
# https://stackoverflow.com/questions/36183486/importerror-no-module-named-google
# https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm
# https://www.hellocodeclub.com/python-speech-recognition-create-program-with-google-api/
#     Getting my API to work
# https://stackoverflow.com/questions/6434482/python-function-overloading
#     Defining a function with a "none" input
