import Person
from Person import PersonClass, makeSlides


class Instructor(Person.PersonClass):
    def task(self):
        Person.makeSlides()


if __name__ == "__main__":
    personA = Instructor("Farukh", "Hummus", ["Mo", "Tim"])
    personA.fav_food()
    personA.task()
