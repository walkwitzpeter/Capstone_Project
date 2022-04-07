import random
from tkinter import *
from PIL import Image, ImageTk

import record_audio
import user_data_management as udm
import tkinter_window
import tkinter.font as font


def open_homepage_window(prev_win=None):
    tk = tkinter_window.TkInterWindow()
    tk.open_basic_window("Speaking with Peter Rabbit", prev_win)
    img = (Image.open("Photos/Homepage Image.png"))
    resized_img = img.resize((1300, 725), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resized_img)

    label = Label(
        tk.window,
        image=img,
        height=tk.window.winfo_screenheight(),
        width=tk.window.winfo_screenwidth()
    )
    label.place(x=0, y=0, relwidth=1, relheight=1)

    my_font_big = font.Font(size=20)
    my_font_small = font.Font(size=15)
    # Play button
    play_btn = Button(tk.window, text="Practice", font=my_font_big,
                      command=lambda: open_category_selection(tk.window))
    play_btn.grid(row=8, rowspan=1, column=3, columnspan=3, ipadx=150, ipady=20)

    # See user data Button
    see_user_stats_btn = Button(tk.window, text="See Stats", font=my_font_small,
                                command=lambda: open_stats(tk.window))
    see_user_stats_btn.grid(row=8, rowspan=1, column=1, columnspan=2, ipadx=125, ipady=20)
    # Instructions Button
    instructions_btn = Button(tk.window, text="Instructions", font=my_font_small,
                              command=lambda: open_instructions(tk.window))
    instructions_btn.grid(row=8, rowspan=1, column=7, columnspan=2, ipadx=125, ipady=20)

    tk.window.mainloop()


def open_instructions(prev_win):
    tk = tkinter_window.TkInterWindow()
    tk.open_basic_window("Instructions", prev_win)

    # Font Sizes
    my_font_big = font.Font(size=30)
    my_font_small = font.Font(size=15)

    # Basic Instructions
    basic_ins_title = Label(
        tk.window,
        text="Basic Instructions",
        font=my_font_big
    )
    basic_ins_title.grid(row=0, column=0, columnspan=8)
    basic_instructions = Label(
        tk.window,
        text="This program is designed to help users practice their speech while providing "
             "feedback on growth over time. The stats button will show you your progress each "
             "day. These graphs average out all exercises of each mode that you did that day. The"
             " number next to each point displays how many questions you completed in total that "
             "day.\n\nTo begin practicing first click 'Practice' on the homepage and then select "
             "your category of words, then select the game mode you would like to play. The modes"
             " are explained down below.",
        font=my_font_small,
        wraplength=1000
    )
    basic_instructions.grid(row=1, column=0, columnspan=8)

    # Canvas so you can scroll
    canvas = Canvas(tk.window)
    canvas_frame = Frame(canvas)

    # Scrollbar
    vscroll = Scrollbar(tk.window, orient="vertical", command=canvas.yview)
    canvas['yscrollcommand'] = vscroll.set
    canvas.grid(row=2, column=2, columnspan=7, sticky="nsew")
    vscroll.grid(row=2, rowspan=6, column=8, sticky="nsew")

    # Game Instructions
    game_ins_title = Label(
        canvas_frame,
        text="Game Mode Instructions",
        font=my_font_big
    )
    game_ins_title.grid(row=0, column=0, columnspan=8)

    # Drop Down Menu callback
    def instruction_callback(*args):
        if 'Typing' in clicked.get():
            game_instructions.config(text=typing_mode_text)
        elif 'Speaking' in clicked.get():
            game_instructions.config(text=speaking_mode_text)
        elif 'Spelling' in clicked.get():
            game_instructions.config(text=spelling_mode_text)

    # Setting up the drop-down menu
    modes = [
        'Select Mode',
        'Typing Mode',
        'Speaking Mode',
        'Spelling Mode'
    ]
    clicked = StringVar(value=modes[0])
    drop = OptionMenu(canvas_frame, clicked, *modes)
    drop.grid(row=1, columnspan=tk.ROWS, column=0)

    speaking_mode_text = "In Speaking Mode the user will be shown a picture after which they record the word that the "\
                         "picture is showing. To record themselves the user clicks the record button and a microphone "\
                         "appears, then click the microphone to begin recording and click again to end the recording."
    typing_mode_text = "In Typing Mode you can both record your answer or type it, we recommend typing the answer " \
                       "first to work on spelling then reading your answer afterwards. Once you hit enter it will " \
                       "check your answer, or if you already answered correctly hitting enter again will take you to " \
                       "the next screen, or you may click the check answer button to check the text entry, and use " \
                       "the arrow to go to the next screen."
    spelling_mode_text = "In Spelling Mode you will be presented with a picture of a word. Then you will be given the" \
                         " corresponding number of blank spaces. Below the blank spaces will be the right letters but" \
                         " in a random order. You will then select the correct letter that needs to go next. Getting " \
                         "one letter wrong counts as getting the whole word wrong, when recording your statistics."
    game_instructions = Label(
        canvas_frame,
        text="Pleas select the game mode from the drop down menu above to see the corresponding explanation.",
        font=my_font_small,
        wraplength=800
    )
    game_instructions.grid(row=2, column=0, columnspan=8)

    # Binding the drop-down menu
    clicked.trace("w", instruction_callback)

    # Create the canvas
    canvas.create_window((0, 0), window=canvas_frame, anchor='n')
    # Binding scrollbar to canvas-frame
    canvas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


def open_game_selection(prev_win, word_category):
    tk = tkinter_window.TkInterWindow()
    tk.open_basic_window("Game Selection", prev_win)

    my_font = font.Font(family='Helvetica', size=20)

    # Making my different activity buttons
    associations_btn = Button(tk.window, text="Speaking Mode",
                              command=lambda: open_basic_association(tk.window, word_category),
                              font=my_font)
    type_say_see_btn = Button(tk.window, text="Typing Mode",
                              command=lambda: open_type_say_see(tk.window, word_category),
                              font=my_font)
    spelling_btn = Button(tk.window, text="Spelling Mode",
                          command=lambda: open_spelling_mode(tk.window, word_category),
                          font=my_font)

    # Putting them on the screen and configuring the Grid
    associations_btn.grid(row=1, rowspan=2, column=1, columnspan=2)
    type_say_see_btn.grid(row=1, rowspan=2, column=5, columnspan=2)
    spelling_btn.grid(row=3, rowspan=2, column=3, columnspan=1)


def open_category_selection(prev_win):
    tk = tkinter_window.TkInterWindow()
    tk.open_basic_window("Categories", prev_win)
    tk.ROWS = 7
    tk.COLUMNS = 7
    tk.back_btn.grid(row=0, rowspan=1, column=0, columnspan=1)

    # The font for the buttons
    my_font = font.Font(family='Helvetica', size=20)
    # Setting up each category button
    food_btn = Button(tk.window, text="Foods", font=my_font,
                      command=lambda: open_game_selection(tk.window, "Food"))
    food_btn.grid(row=1, rowspan=2, column=1, columnspan=2)
    color_btn = Button(tk.window, text="Colors", font=my_font,
                       command=lambda: open_game_selection(tk.window, "Color"))
    color_btn.grid(row=1, rowspan=2, column=5, columnspan=2)

    all_btn = Button(tk.window, text="All Categories", font=my_font,
                     command=lambda: open_game_selection(tk.window, "All"))
    all_btn.grid(row=3, rowspan=2, column=3, columnspan=2)

    object_btn = Button(tk.window, text="Objects", font=my_font,
                        command=lambda: open_game_selection(tk.window, "Object"))
    object_btn.grid(row=5, rowspan=2, column=1, columnspan=2)
    body_part_btn = Button(tk.window, text="Body Parts", font=my_font,
                           command=lambda: open_game_selection(tk.window, "Body"))
    body_part_btn.grid(row=5, rowspan=2, column=5, columnspan=2)


def open_stats(prev_win):
    # My call back function to change graphs on drop down menu
    def graph_callback(*args):
        if 'Typing' in clicked.get():
            type_figure.grid()
            ass_figure.grid_remove()
            spelling_figure.grid_remove()
        elif 'Speaking' in clicked.get():
            type_figure.grid_remove()
            ass_figure.grid()
            spelling_figure.grid_remove()
        elif 'Spelling' in clicked.get():
            type_figure.grid_remove()
            ass_figure.grid_remove()
            spelling_figure.grid()
        else:
            type_figure.grid_remove()
            ass_figure.grid_remove()
            spelling_figure.grid_remove()

    tk = tkinter_window.TkInterWindow()
    tk.open_basic_window("User Stats", prev_win)

    # Setting up the drop-down menu
    graphs = [
        'Select Graph',
        'Typing Mode',
        'Speaking Mode',
        'Spelling Mode'
    ]
    clicked = StringVar(value=graphs[0])
    drop = OptionMenu(tk.window, clicked, *graphs)
    drop.grid(row=0, columnspan=tk.ROWS, column=0)

    # Setting up the graph for associations option
    udm.find_stats("Output_Files/associations_user_percentages.csv")
    associations_graph = udm.get_plot(tk.window, "Speaking Mode")
    ass_figure = associations_graph.get_tk_widget()
    # Placing so it retains proper position, then removing
    ass_figure.grid(row=2, column=0, columnspan=tk.COLUMNS)
    ass_figure.grid_remove()

    # Setting up the graph for TSS option
    udm.find_stats("Output_Files/tss_user_percentages.csv")
    typing_graph = udm.get_plot(tk.window, "Typing Mode")
    type_figure = typing_graph.get_tk_widget()
    # Placing so it retains proper position, then removing
    type_figure.grid(row=2, column=0, columnspan=tk.COLUMNS)
    type_figure.grid_remove()

    # Setting up graph for Spelling option
    udm.find_stats("Output_Files/spelling_user_percentages.csv")
    spelling_graph = udm.get_plot(tk.window, "Spelling Mode")
    spelling_figure = spelling_graph.get_tk_widget()
    # Placing so it retains proper position, then removing
    spelling_figure.grid(row=2, column=0, columnspan=tk.COLUMNS)
    spelling_figure.grid_remove()

    # Calling my callback function
    clicked.trace("w", graph_callback)


def open_basic_association(prev_win, category):
    # Running my Basic Game Window
    tk = tkinter_window.TkInterWindow()
    tk.open_game_window(prev_win, "Basic Associations", category, "Associations")

    # Setting up the record button
    tk.record_audio_btn = Button(tk.window, text="Record Answer",
                                 command=lambda: record_audio.RecAUD())
    tk.record_audio_btn.grid(row=4, column=4)
    # Checking the recording
    tk.check_recording_btn = Button(tk.window, text="Check Recording",
                                    command=lambda: tk.check_recording())
    tk.check_recording_btn.grid(row=4, column=5)


def open_type_say_see(prev_win, category):
    # Tk Variables
    tk = tkinter_window.TkInterWindow()
    tk.open_game_window(prev_win, "Type Say See Hear", category, "TSS")

    # Set up the input typing
    entry = Entry(tk.window, width=50)
    entry.focus_set()
    entry.grid(row=3, column=3, columnspan=4)
    # This is used to let the user check their answer with the enter key
    entry.bind('<Key-Return>', lambda *_args: tk.enter_func(entry))

    check_entry_btn = Button(tk.window, text="Check Answer",
                             command=lambda: tk.check_text_entry(entry))
    check_entry_btn.grid(row=4, column=4, columnspan=2)

    # Clearing the user's entry on next button press
    tk.next_arw_btn["command"] = lambda: tk.get_next_screen(entry)


def open_spelling_mode(prev_win, category):
    tk = tkinter_window.TkInterWindow()
    tk.open_game_window(prev_win, "Spelling Practice", category, "Spelling")

    tk.spelling = True

    setup_spelling(tk)


def setup_spelling(tk):
    my_font = font.Font(family='Helvetica', size=30, underline=True)
    word_string = tk.cur_answer.upper()
    start_pos = int(tk.COLUMNS/2 - len(word_string)/2 + 1)
    # Randomizing letters
    cur_positions = []
    rand = random.Random()
    for letter_pos in range(len(word_string)):
        cur_letter = str(word_string[letter_pos])
        ltr_label = Label(tk.window, text=" ", font=my_font)
        ltr_label.grid(row=3, column=start_pos + letter_pos)

        ltr_btn = Button(tk.window, text=cur_letter, font=my_font)
        ltr_btn.configure(command=lambda label=ltr_label, letter=cur_letter, btn=ltr_btn:
                          tk.change_label(letter, label, btn))
        # Randomizing the placement of the letters
        placement = rand.randint(start_pos, start_pos + len(word_string) - 1)
        while placement in cur_positions:
            placement = rand.randint(start_pos, start_pos + len(word_string) - 1)
        ltr_btn.grid(row=4, column=placement)
        cur_positions.append(placement)


if __name__ == '__main__':
    open_homepage_window()


# Sources (description below the links)
# Main Sources
# https://docs.python.org/3/library/tkinter.html - documentation for tkinter
# https://stackoverflow.com - questions
# https://www.geeksforgeeks.org - basic tutorials
# https://www.hellocodeclub.com - google api


# Everything
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
# https://icons8.com/icon/By2nLkSnm99A/foot-emoji
# https://iconscout.com/icon/arm-edema-3589321
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
# Music by <a href="/users/beetpro-16097074/?tab=audio&amp;utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=audio&amp;utm_content=11282">beetpro</a> from <a href="https://pixabay.com/music/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=11282">Pixabay</a>
#     Fail Sound
# Music from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6297">Pixabay</a>
#     Success Sound
