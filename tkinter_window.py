from tkinter import *
from datetime import date

import pygame
import word_image_dictionary
import google_api
import main
import record_audio

import tkinter.font as font


def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


class TkInterWindow:
    def __init__(self):
        # Constants for my grid
        self.ROWS = 8
        self.COLUMNS = 8

        # File path strings for sounds
        self.success_sound_path = "Sounds/success.mp3"

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
        self.right = False

    def open_basic_window(self, title, prev_win=None):
        if prev_win is not None:
            prev_win.destroy()
        self.window = Tk()
        self.window.geometry("800x500")
        self.window.state('zoomed')
        self.window.title(title)

        # Making my grid
        for row_number in range(self.ROWS):
            Grid.rowconfigure(self.window, row_number, weight=4)
        for column_number in range(self.COLUMNS):
            Grid.columnconfigure(self.window, column_number, weight=4)

        # Place a back arrow
        self.back_arw_img = PhotoImage(master=self.window, file="Photos/Back Arrow.png").subsample(7, 7)
        self.back_btn = Button(self.window, text="Back",
                               command=lambda: self.go_back("NA"),
                               image=self.back_arw_img)
        self.back_btn.grid(row=0, column=0)
        # Making its part of the grid smaller than the other parts
        Grid.rowconfigure(self.window, 0, weight=1)
        Grid.columnconfigure(self.window, 0, weight=1)

    def open_game_window(self, prev_win, title, category, game_mode):
        prev_win.destroy()
        self.window = Tk()
        self.window.state('zoomed')
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
                               command=lambda: self.go_back(game_mode),
                               image=self.back_arw_img)
        self.back_btn.grid(row=0, column=0)
        self.next_arw_img = PhotoImage(master=self.window, file=r"Photos/Next Arrow.png").subsample(9, 9)
        self.next_arw_btn = Button(self.window, text="Next",
                                   command=lambda: self.get_next_screen(),
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
        user_text = user_input.get().casefold()
        if user_text == self.photos_and_answers.curAnswer.casefold():
            # play_sound(self.success_sound_path)
            self.feedback_text['text'] = "Correct!"
            self.feedback_text['image'] = self.check_img
            self.right = True
            self.update_counts()
        else:
            self.feedback_text['text'] = "Incorrect"
            self.feedback_text['image'] = self.x_img
            self.right = False
            self.update_counts()
        self.feedback_text.grid()

    def check_recording(self):
        text = str(google_api.GoogleAPI().get_transcript())
        self.feedback_text['text'] = "We heard the following possibilities:\n" + text
        self.feedback_text.grid()
        print("cur_answer: " + self.photos_and_answers.curAnswer)
        if text.casefold().__contains__(self.photos_and_answers.curAnswer.casefold()):
            play_sound(self.success_sound_path)
            self.feedback_text['image'] = self.check_img
            self.right = True
            self.update_counts()
        else:
            self.feedback_text['image'] = self.x_img
            self.right = False
            self.update_counts()

    def update_counts(self):
        if not self.checked:
            if self.right:
                self.words_correct += 1
                play_sound(self.success_sound_path)
            self.words_attempted += 1
            self.checked = True
            print(str(self.words_correct) + "Correct")
            print(str(self.words_attempted) + "Attempted")

    def get_next_screen(self, entry=None):
        # To see if they attempted the question
        if self.checked:
            # Changing image if there is another image waiting and update answer
            if self.photos_and_answers.imgStack:
                if entry is not None:
                    entry.delete(0, END)
                img = self.photos_and_answers.imgStack.pop()
                self.main_img.configure(image=img)
                self.main_img.image = img
                self.photos_and_answers.updateCurAnswer()
                self.feedback_text.grid_remove()
                self.checked = False
            elif self.checked:
                print("feedback screen")
                self.open_basic_window(prev_win=self.window, title="Feedback Window")
                my_font = font.Font(family='Helvetica', size=40)
                score_text = "You got " + str(self.words_correct) + "/" + str(self.words_attempted) + \
                             " word(s) correct."
                score = Label(self.window, text="Congratulations you finished!\n" + score_text +
                                                "\n Lets keep practicing!",
                              font=my_font)
                score.grid(row=1, rowspan=self.ROWS-1, column=1, columnspan=self.COLUMNS-1)

    def go_back(self, game_mode):
        # Append percentage right to txt file
        if self.words_attempted > 0:
            self.percentage_right = self.words_correct/self.words_attempted
            if game_mode == "Associations":
                with open("Output_Files/associations_user_percentages.csv", "a") as file_object:
                    print("associations")
                    file_object.write(str(self.words_attempted) + "," + str(self.percentage_right * 100) + "," +
                                      str(date.today())
                                      + "\n")
            else:
                with open("Output_Files/tss_user_percentages.csv", "a") as file_object:
                    print("tss")
                    file_object.write(str(self.words_attempted) + "," + str(self.percentage_right * 100) + "," +
                                      str(date.today())
                                      + "\n")
        # Go Back to Homepage
        main.open_homepage_window(self.window)

    def enter_func(self, entry):
        if self.checked and self.right:
            self.get_next_screen(entry)
        else:
            self.check_text_entry(entry)

    def close_window(self):
        self.window.destroy()
