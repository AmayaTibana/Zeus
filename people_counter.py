class PeopleCounter:
    x = 0

    def anotherOne(self) :
        self.x = self.x + 1
        print("So far", self.x)
people = PeopleCounter()
people.anotherOne()
people.anotherOne()
people.anotherOne()
people.anotherOne()