class cat:
    height=100
    satiety=60
    age=11

class dog(cat):
    age = 7

class turtle(cat):
    satiety = 50

    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)
nick = turtle()