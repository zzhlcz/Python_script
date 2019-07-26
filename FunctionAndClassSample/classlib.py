class Dog:
    def __init__(self, localname, localage):
        self.name = localname
        self.age = localage
        self.mile = 0

    def sit(self):
        print(self.name + "is now sitting")

    def roll_over(self):
        print(self.name + "rolled over")


class Happyhere:
    def __init__(self, localhappyhour = 70):
        self.happyhour = localhappyhour

    def printhappyhour(self):
        print(self.happyhour)


class Happydog(Dog):
    def __init__(self, localname, localage):
        super().__init__(localname, localage)
        self.happyhour = Happyhere()

