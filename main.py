import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
import PySimpleGUI as GUI


def record_sound():

    print("Ready to record?")
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file
    print("Recorded?")
    playsound('output.wav')
    print("played?")


def open_window():
    # TODO figure out how to resize this (to start with just to the size of the screen)
    layout = [[GUI.Text("Welcome to MySpeechTherapy")], [GUI.Button("Start")], [GUI.Button("Exit")]]

    # Create the window
    window = GUI.Window("Demo", layout, margins=(400, 200))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Exit" or event == GUI.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    open_window()
    # record_sound()

# Sources
# https://realpython.com/playing-and-recording-sound-python/#recording-audio
#     Used for how to record and playback audio

