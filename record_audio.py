# Import the necessary modules.
import tkinter
import tkinter as tk
import tkinter.messagebox
import pyaudio
import wave
import os
"""
Code taken from
https://stackoverflow.com/questions/43521804/recording-audio-with-pyaudio-on-a-button-click-and-stop-recording-on-another-but
"""


class RecAUD:
    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):
        # Start Tkinter and set Title
        self.main = tkinter.Tk()
        self.collections = []

        # Setting the location of my window
        w = 150  # width for the Tk root
        h = 150  # height for the Tk root

        # get screen width and height
        ws = self.main.winfo_screenwidth()  # width of the screen
        hs = self.main.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.main.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # Used to get rid of titlebar
        self.main.overrideredirect(True)

        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 0
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,
                                  frames_per_buffer=self.CHUNK)

        # Set Frames
        # self.buttons = tkinter.Frame(self.main)

        # Pack Frame
        # self.buttons.pack(fill=tk.BOTH)

        # Start and Stop buttons
        mic_image = tkinter.PhotoImage(master=self.main, file=r"mic_image.png").subsample(3, 3)
        # self.strt_rec = tkinter.Button(self.buttons, padx=10, pady=5, text='Start Recording',
        #                                command=lambda: self.start_record(), image=mic_image)
        self.strt_rec = tkinter.Button(self.main, command=lambda: self.start_record(), image=mic_image,
                                       width=150, height=150)
        self.strt_rec.grid(row=0, column=0, sticky='nsew')
        # self.stop_rec = tkinter.Button(self.buttons, text='Stop Recording', command=lambda: self.stop())
        # self.stop_rec.grid(row=1, column=0)

        tkinter.mainloop()

    def start_record(self):
        if self.st == 1:
            self.st = 0
        else:
            self.st = 1
            self.frames = []
            stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,
                                 frames_per_buffer=self.CHUNK)
            while self.st == 1:
                data = stream.read(self.CHUNK)
                self.frames.append(data)
                print("* recording")
                self.main.update()

            stream.close()

            wf = wave.open('test_recording.wav', 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            self.main.destroy()

    def stop(self):
        self.st = 0

