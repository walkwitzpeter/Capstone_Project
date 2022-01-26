from playsound import playsound


class MySpider:
    def __init__(self):
        self.legs = 8
        self.weight = 0

    def lose_leg(self):
        self.legs -= 1


print("start test")
spider1 = MySpider()
print(spider1.legs)
spider1.lose_leg()
print(spider1.legs)

playsound(r'C:\Users\Peter Walkwitz\PyCharm_Capstone\MySpeechTherapy\test_recording.wav')
