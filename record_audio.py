# Import the necessary modules.
import tkinter
import tkinter as tk
import tkinter.messagebox
import pyaudio
import wave
import os

from pynput.mouse import Controller


"""
Code taken from
https://stackoverflow.com/questions/43521804/recording-audio-with-pyaudio-on-a-button-click-and-stop-recording-on-another-but
"""


class RecAUD:
    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):
        # Start Tkinter and set Title
        self.main = tkinter.Tk()
        # TODO
        # Setting this window the only clickable (doesnt actually work)
        # self.main.grab_set()
        self.collections = []
        self.mouse = Controller()

        # Width and height of my popup window
        w = 150
        h = 150

        # Get mouse position
        self.mouse_x = self.mouse.position[0]
        self.mouse_y = self.mouse.position[1]

        # Calculate x and y coordinates for the Tk root window
        x = self.mouse_x - (w / 2)
        y = self.mouse_y - (h / 2)

        # Set the dimensions of the screen and where it is placed
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

        # Mic Button
        mic_image = tkinter.PhotoImage(master=self.main, file=r"Photos/mic_image.png").subsample(3, 3)
        self.strt_rec = tkinter.Button(self.main, command=lambda: self.start_record(), image=mic_image,
                                       width=w, height=h)
        self.strt_rec.grid(row=0, column=0, sticky='nsew')

        tkinter.mainloop()

    def set_mouse_x(self, mouse_positions):
        self.mouse_x = mouse_positions[0]

    def set_mouse_y(self, mouse_positions):
        self.mouse_y = mouse_positions[1]

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

            wf = wave.open('Output_Files/audio_recording.wav', 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            # TODO not working
            # self.main.grab_release()
            self.main.destroy()

    def stop(self):
        self.st = 0

