import random
from tkinter import PhotoImage

FoodWords = ['Apple', 'Orange', 'Carrot', 'Rice', 'Raisin']
ColorWords = ['Red', 'Green', 'Blue', 'Pink', 'Black']
ObjectWords = ['Radio', 'Rocket', 'Wrench', 'Rock', 'Computer']
BodyWords = ['Hand', 'Foot']
AllWords = FoodWords + ColorWords + ObjectWords + BodyWords


class Words:
    def __init__(self):
        self.__wordStack = []
        self.imgStack = []
        self.curAnswer = ""

        # Used to randomize the list
        self.rand = random.Random()
        self.position_array = []

    def initializeStacks(self, category):
        if category == "Food":
            chosen_array = FoodWords
        elif category == "Color":
            chosen_array = ColorWords
        elif category == "Object":
            chosen_array = ObjectWords
        elif category == "Body":
            chosen_array = BodyWords
        elif category == "All":
            chosen_array = AllWords
        else:
            print("Failed to find category")
            chosen_array = AllWords

        # Adding words and Images to stack
        for word in chosen_array:
            # Randomizing the word order
            rand_word_pos = self.rand.randint(0, len(chosen_array) - 1)
            while rand_word_pos in self.position_array:
                rand_word_pos = self.rand.randint(0, len(chosen_array) - 1)
            self.position_array.append(rand_word_pos)
            # Making the word random instead of in order with the below assignment
            word = chosen_array[rand_word_pos]
            self.__wordStack.append(word)
            img = PhotoImage(file="Photos/" + word + ".png").subsample(2, 2)
            self.imgStack.append(img)

    def updateCurAnswer(self):
        self.curAnswer = self.__wordStack.pop()
