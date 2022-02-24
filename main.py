from tkinter import *
import user_data_management as udm
import tkinter_window
import tkinter.font as font


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

    # Play button
    play_btn = Button(window, text="Practice", command=lambda: open_category_selection(window))
    play_btn.grid(row=3, rowspan=2, column=0, columnspan=2)

    # # Making my different activity buttons
    # associations_btn = Button(window, text="Basic Associations", command=lambda: open_basic_association(window))
    # type_say_see_btn = Button(window, text="Type, Say, See", command=lambda: open_type_say_see(window))
    #
    # # Putting them on the screen and configuring the Grid
    # associations_btn.grid(row=0, rowspan=2, column=0, columnspan=2)
    # type_say_see_btn.grid(row=1, rowspan=2, column=0, columnspan=2)

    # Organizing the grid for my button layout
    for row_number in range(3):
        Grid.rowconfigure(window, row_number, weight=1)
    # for column_number in range(4):
    #     Grid.columnconfigure(window, column_number, weight=1)

    # See user data Buttons
    see_user_stats_btn = Button(window, text="See Stats", command=lambda: open_stats(window))
    see_user_stats_btn.grid(row=2, rowspan=2, column=0, columnspan=2)

    window.mainloop()


def open_game_selection(prev_win, word_category):
    tk = tkinter_window.TkInterWindow()
    tk.open_basic_window(prev_win, "Game Selection")

    # Making my different activity buttons
    associations_btn = Button(tk.window, text="Basic Associations",
                              command=lambda: open_basic_association(tk.window, word_category))
    type_say_see_btn = Button(tk.window, text="Type, Say, See",
                              command=lambda: open_type_say_see(tk.window, word_category))

    # Putting them on the screen and configuring the Grid
    associations_btn.grid(row=0, rowspan=2, column=0, columnspan=2)
    type_say_see_btn.grid(row=1, rowspan=2, column=0, columnspan=2)


def open_category_selection(prev_win):
    tk = tkinter_window.TkInterWindow()
    tk.open_basic_window(prev_win, "Categories")
    tk.ROWS = 7
    tk.COLUMNS = 7
    tk.back_btn.grid(row=0, rowspan=1, column=0, columnspan=1)

    # Setting up each category button
    my_font = font.Font(family='Helvetica', size=20)
    food_btn = Button(tk.window, text="Foods", font=my_font,
                      command=lambda: open_game_selection(tk.window, "Food"))
    food_btn.grid(row=1, rowspan=2, column=1, columnspan=2)
    color_btn = Button(tk.window, text="Colors", font=my_font,
                       command=lambda: open_game_selection(tk.window, "Color"))
    color_btn.grid(row=1, rowspan=2, column=5, columnspan=2)

    all_btn = Button(tk.window, text="All Categories", font=my_font)
    all_btn.grid(row=3, rowspan=2, column=3, columnspan=2)

    object_btn = Button(tk.window, text="Objects", font=my_font,
                        command=lambda: open_game_selection(tk.window, "Object"))
    object_btn.grid(row=5, rowspan=2, column=1, columnspan=2)
    body_part_btn = Button(tk.window, text="Body Parts", font=my_font,
                           command=lambda: open_game_selection(tk.window, "Body Part"))
    body_part_btn.grid(row=5, rowspan=2, column=5, columnspan=2)


def open_stats(prev_win):
    tk = tkinter_window.TkInterWindow()
    tk.open_basic_window(prev_win, "User Stats")

    udm.find_stats()
    graph = udm.get_plot(tk.window)
    graph.get_tk_widget().grid(row=1, rowspan=tk.ROWS - 1, column=1, columnspan=tk.COLUMNS-1)


def open_basic_association(prev_win, category):
    # Running my Basic Game Window
    tk = tkinter_window.TkInterWindow()
    tk.open_game_window(prev_win, "Basic Associations", category)


def open_type_say_see(prev_win, category):
    # Tk Variables
    tk = tkinter_window.TkInterWindow()
    tk.open_game_window(prev_win, "Type Say See Hear", category)

    # Set up the input typing
    entry = Entry(tk.window, width=50)
    entry.focus_set()
    entry.grid(row=3, column=3, columnspan=4)
    check_entry_btn = Button(tk.window, text="Check Answer",
                             command=lambda: tk.check_text_entry(entry))
    check_entry_btn.grid(row=5, column=3, columnspan=2)

    # Seeing the correct answer
    see_answer_btn = Button(tk.window, text="See Answer",
                            command=lambda: tk.see_answer())
    see_answer_btn.grid(row=5, column=5, columnspan=2)

    # Hiding the buttons I don't want shown
    tk.record_audio_btn.grid_remove()
    tk.check_recording_btn.grid_remove()


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
# https://www.tutorialspoint.com/taking-input-from-the-user-in-tkinter#:~:text=We%20can%20get%20the%20user,help%20of%20the%20Label%20widget
# https://pythonexamples.org/python-tkinter-button-change-font/
#     Used for TKinter basics
# https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
# https://twitter.com/humanbrainproj/status/1233727365768974336?lang=eu
# https://www.iconfinder.com/icons/329731/back_arrow_left_previous_return_icon
# https://commons.wikimedia.org/wiki/File:Apple_icon_1.png
# https://www.pngwing.com/en/free-png-kqaob
# https://www.iconsdb.com/green-icons/check-mark-3-icon.html
# https://www.dictionary.com/e/emoji/cross-mark-emoji/
# https://shop.passionfoods.com.au/search?q%5B%5D=category%3Awheat&sort_by=discount_percent
# https://houseofhealthcollective.com.au/category/dried-fruit-nuts
# https://www.pinterest.com/pin/free-orange-radio-2-icon-download-orange-radio-2-icon--613404411743203644/
# https://www.crunchbase.com/organization/done-38e9
# https://www.iconsdb.com/blue-icons/microphone-icon.html
# https://stackoverflow.com/questions/10158552/how-to-use-an-image-for-the-background-in-tkinter
# https://www.iconsdb.com/orange-icons/radio-2-icon.html
# https://www.iconsdb.com/green-icons/square-icon.html
# https://visualidentity.columbia.edu/content/colors-1
# https://www.iconsdb.com/deep-pink-icons/square-icon.html
# https://constructarcade.com/game/back-to-space/
# https://www.iconsdb.com/custom-color/computer-icon.html
# https://www.iconsdb.com/black-icons/wrench-2-icon.html
# https://www.iconsdb.com/black-icons/rocket-icon.html
# https://www.vexels.com/png-svg/preview/145829/rubble-illustration
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
# https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
#     Writing to the end of a file in python (just wanted to double check I did this right)
# https://datatofish.com/matplotlib-charts-tkinter-gui/
# https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/
#     How to do charts for user data
# https://www.geeksforgeeks.org/get-current-date-using-python/
#     Current date in python
