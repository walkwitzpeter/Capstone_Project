import json
from tkinter import PhotoImage

ArrayOfWords = ['Done', 'Apple', 'Orange', 'Carrot', 'Red', 'Rice', 'Radio', 'Raisin']

WordImageDictionary = {
    'Done': 'Done.png',
    'Apple': 'Apple.png',
    'Orange': 'Orange.png',
    'Carrot': 'Carrot.png',
    'Red': 'Red.png',
    'Rice': 'Rice.png',
    'Radio': 'Radio.png',
    'Raisin': 'Raisin.png'
}


class Words:
    def __init__(self):
        self.__wordStack = []
        self.imgStack = []
        self.curAnswer = ""

    def initializeStacks(self):
        for word in ArrayOfWords:
            self.__wordStack.append(word)
            img = PhotoImage(file="Photos/" + WordImageDictionary[word]).subsample(2, 2)
            self.imgStack.append(img)

    def updateCurAnswer(self):
        self.curAnswer = self.__wordStack.pop()


# rocket
# ranch
# rich
# race
# ring
# rain
# rug
# ran
# write
# rip
# recess
# rock
# read
# wrap
