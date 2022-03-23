from tkinter import PhotoImage

# AllWords = ['Apple', 'Orange', 'Carrot', 'Red', 'Rice', 'Radio', 'Raisin', 'Green', 'Blue', 'Pink', 'Black',
#             'Rocket', 'Wrench', 'Rock', 'Computer']
FoodWords = ['Apple', 'Orange', 'Carrot', 'Rice', 'Raisin']
ColorWords = ['Red', 'Green', 'Blue', 'Pink', 'Black']
ObjectWords = ['Radio', 'Rocket', 'Wrench', 'Rock', 'Computer']
BodyWords = ['Hand', 'Foot']
AllWords = FoodWords + ColorWords + ObjectWords + BodyWords

# WordImageDictionary = {
#     'Done': 'Done.png',
#     'Apple': 'Apple.png',
#     'Orange': 'Orange.png',
#     'Carrot': 'Carrot.png',
#     'Red': 'Red.png',
#     'Rice': 'Rice.png',
#     'Radio': 'Radio.png',
#     'Raisin': 'Raisin.png',
#     'Green': 'Green.png',
#     'Blue': 'Blue.png',
#     'Pink': 'Pink.png',
#     'Black': 'Black.png',
#     'Rocket': 'Rocket.png',
#     'Wrench': 'Wrench.png',
#     'Rock': 'Rock.png',
#     'Computer': 'Computer.png'
# }

# category = "All"


class Words:
    def __init__(self):
        self.__wordStack = []
        self.imgStack = []
        self.curAnswer = ""

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

        for word in chosen_array:
            self.__wordStack.append(word)
            img = PhotoImage(file="Photos/" + word + ".png").subsample(2, 2)
            self.imgStack.append(img)

    def updateCurAnswer(self):
        self.curAnswer = self.__wordStack.pop()
