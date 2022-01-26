import time
import pyaudio

import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
from tkinter import *
import record_audio

# TODO google api to send it what I record and see if it works?omcd py  
# TODO python library for speech comparison?


def open_window():
    window = Tk()
    window.title('My Speech Therapy Project')
    window.geometry("800x500")
    window.resizable()

    # Making my buttons to record audio
    exit_button = Button(window, text="Exit", command=lambda: window.destroy())
    record_audio_btn = Button(window, text="Start Recording", command=lambda: record_audio.RecAUD())
    # stop_recording_audio = Button(window, text="Stop Recording", command=lambda: start_recording(audioObject))

    # Putting my buttons on the screen, and configuring the Grid
    record_audio_btn.grid(row=0, column=0, columnspan=2)
    # stop_recording_audio.grid(row=0, column=2, columnspan=2)
    exit_button.grid(row=1, column=1, columnspan=2)

    # Organizing the grid for my button layout
    for row_number in range(2):
        Grid.rowconfigure(window, row_number, weight=1)
    for column_number in range(4):
        Grid.columnconfigure(window, column_number, weight=1)

    window.mainloop()


if __name__ == '__main__':
    open_window()
    # record_sound()

# Sources
# https://realpython.com/playing-and-recording-sound-python/#recording-audio
#     Used for how to record and playback audio
# https://www.daniweb.com/programming/software-development/threads/426702/problem-in-music-player
#     Used to fix my error when trying to play the sound
# https://www.youtube.com/watch?v=NytF3pJSMc8&ab_channel=Codemy.com
#     Used for TKinter basics (And other Codemy.com videos on youtube)
# https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
#     Used for images on a tkinter button
# https://www.iconsdb.com/blue-icons/microphone-icon.html
#     Used for my microphone image
# https://stackoverflow.com/questions/30786337/tkinter-windows-how-to-view-window-in-windows-task-bar-which-has-no-title-bar/30819099#30819099
#     Used to get rid of titlebar
# https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
#     Used to move my window to open at a certain location
