from tkinter import *
from datetime import date

import word_image_dictionary
import google_api
import main
import record_audio


class TkInterWindow:
    def __init__(self):
        # Constants for my grid
        self.ROWS = 8
        self.COLUMNS = 8

        # Setting up the different variables for my window
        self.window = None
        self.feedback_text = None

        # Buttons
        self.back_btn = None
        self.next_arw_btn = None
        self.record_audio_btn = None
        self.check_recording_btn = None

        # Image
        self.back_arw_img = None
        self.next_arw_img = None
        self.main_img = None
        self.check_img = None
        self.x_img = None

        # Answer/Img Stack
        self.photos_and_answers = None

        # Keeping track of percentage correct
        self.words_attempted = 0
        self.words_correct = 0
        self.percentage_right = 0
        self.checked = False

    #TODO
    # Separate all of the words into different categories
    # Click on what category you want after selecting the game mode? or before?
    # Possibly update the user data to keep track of the catagories and how each catagory is doing with the words

    def open_basic_window(self, prev_win, title):
        prev_win.destroy()
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("800x500")

        # Making my grid
        for row_number in range(self.ROWS):
            Grid.rowconfigure(self.window, row_number, weight=4)
        for column_number in range(self.COLUMNS):
            Grid.columnconfigure(self.window, column_number, weight=4)

        # Place a back arrow
        self.back_arw_img = PhotoImage(master=self.window, file="Photos/Back Arrow.png").subsample(7, 7)
        self.back_btn = Button(self.window, text="Back",
                               command=lambda: self.go_back(),
                               image=self.back_arw_img)
        self.back_btn.grid(row=0, column=0)
        # Making its part of the grid smaller than the other parts
        Grid.rowconfigure(self.window, 0, weight=1)
        Grid.columnconfigure(self.window, 0, weight=1)

    def open_game_window(self, prev_win, title, category):
        prev_win.destroy()
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("800x500")

        # Correct and Incorrect Feedback Images
        self.x_img = PhotoImage(file="Photos/Red X.png").subsample(9, 9)
        self.check_img = PhotoImage(file="Photos/Green Check.png").subsample(9, 9)

        # Creating something to keep track of what the current answer is and load photos
        self.photos_and_answers = word_image_dictionary.Words()
        self.photos_and_answers.initializeStacks(category)

        # Making my grid to place items
        for row_number in range(self.ROWS):
            Grid.rowconfigure(self.window, row_number, weight=2)
        for column_number in range(self.COLUMNS):
            Grid.columnconfigure(self.window, column_number, weight=2)

        # Setting up the main image
        img = self.photos_and_answers.imgStack.pop()
        self.photos_and_answers.updateCurAnswer()
        self.main_img = Label(self.window)
        self.main_img.configure(image=img)
        self.main_img.image = img
        self.main_img.grid(row=1, rowspan=2, column=3, columnspan=3)

        # Placing the feedback text box
        self.feedback_text = Label(self.window, text="Your answer appears here", compound=LEFT)
        self.feedback_text.grid(row=6, column=4, columnspan=2)

        # Placing my back and next arrows
        self.back_arw_img = PhotoImage(master=self.window, file=r"Photos/Back Arrow.png").subsample(7, 7)
        self.back_btn = Button(self.window, text="Back",
                               command=lambda: self.go_back(),
                               image=self.back_arw_img)
        self.back_btn.grid(row=0, column=0)
        self.next_arw_img = PhotoImage(master=self.window, file=r"Photos/Next Arrow.png").subsample(9, 9)
        self.next_arw_btn = Button(self.window, text="Next",
                                   command=lambda: self.next_image(),
                                   image=self.next_arw_img)
        self.next_arw_btn.grid(row=self.ROWS, column=self.COLUMNS)
        # Making their part of the grid smaller than the other parts
        Grid.rowconfigure(self.window, 0, weight=1)
        Grid.columnconfigure(self.window, 0, weight=1)

        # Setting up the record button
        self.record_audio_btn = Button(self.window, text="Record Answer",
                                       command=lambda: record_audio.RecAUD())
        self.record_audio_btn.grid(row=4, column=4)
        # Checking the recording
        self.check_recording_btn = Button(self.window, text="Check Recording",
                                          command=lambda: self.check_recording())
        self.check_recording_btn.grid(row=4, column=5)

    def see_answer(self):
        self.feedback_text['text'] = self.photos_and_answers.curAnswer
        self.feedback_text['image'] = ""
        self.feedback_text.grid()

    def check_text_entry(self, user_input):
        user_text = user_input.get()
        if user_text == self.photos_and_answers.curAnswer:
            self.feedback_text['text'] = "Correct!"
            self.feedback_text['image'] = self.check_img
            self.record_audio_btn.grid()
            self.check_recording_btn.grid()
            self.update_counts(right_answer=True)
        else:
            self.feedback_text['text'] = "Incorrect"
            self.feedback_text['image'] = self.x_img
            self.update_counts()
        self.feedback_text.grid()

    def update_counts(self, right_answer=False):
        if not self.checked:
            if right_answer:
                self.words_correct += 1
            self.words_attempted += 1
            self.checked = True
            print(str(self.words_correct) + "Correct")
            print(str(self.words_attempted) + "Attempted")

    def next_image(self):
        # Changing image if there is another image waiting and update answer
        if self.photos_and_answers.imgStack:
            img = self.photos_and_answers.imgStack.pop()
            self.main_img.configure(image=img)
            self.main_img.image = img
            self.photos_and_answers.updateCurAnswer()
            self.feedback_text.grid_remove()
            self.checked = False

    def check_recording(self):
        text = str(google_api.GoogleAPI().get_transcript())
        self.feedback_text['text'] = "We heard the following possibilities:\n" + text
        self.feedback_text.grid()
        print("cur_answer: " + self.photos_and_answers.curAnswer)
        if text.casefold().__contains__(self.photos_and_answers.curAnswer.casefold()):
            self.feedback_text['image'] = self.check_img
            self.update_counts(right_answer=True)
        else:
            self.feedback_text['image'] = self.x_img
            self.update_counts()

    def go_back(self):
        # Append percentage right to txt file
        if self.words_attempted > 0:
            self.percentage_right = self.words_correct/self.words_attempted
            with open("Output_Files/user_percentages.csv", "a") as file_object:
                file_object.write(str(self.words_attempted) + "," + str(self.percentage_right * 100) + "," +
                                  str(date.today())
                                  + "\n")
        # Go Back to Homepage
        main.open_homepage_window(self.window)

    def close_window(self):
        self.window.destroy()
