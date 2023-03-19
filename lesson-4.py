class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in{self.brand}")

nick = Human("Nick")
anna = Human("Anna")
kate = Human("kate")
vasya = Human("Vasya")
nikita = Human("Nikita")
kik = Human("Kik")
car1 = Auto("BMV")
car2 = Auto("Audi")
car3 = Auto("Hyundai")
car2.add_passengers(nick)
car2.add_passengers(kate)
car2.add_passengers(vasya)
car2.add_passengers(nikita)
car1.add_passengers(anna)
car1.add_passengers(kate)
car1.add_passengers(nick)
car3.add_passengers(nikita)
car3.add_passengers(vasya)
car3.add_passengers(kik)
car1.print_passengers_names()
car2.print_passengers_names()
car3.print_passengers_names()