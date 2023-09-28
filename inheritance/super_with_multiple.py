class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        return "bhau bhau"


class Cat(Animal):
    def __init__(self, name, species,age):
        super().__init__(name, species)
        self.age=age

    def make_sound(self):
        return f"Meow and is {self.age}"

class Horse(Animal):
    def __init__(self,name,species):
        super( ).__init__(name,species)

    def make_sound(self):
        return  "neigh"


dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat","old")
horse=Horse("Pony", "Horse")

print(f"{dog.name} the {dog.species} says: {dog.make_sound()}")
print(f"{cat.name} the {cat.species} says: {cat.make_sound()}")
print(f"{horse.name} the {horse.species} says: {horse.make_sound()}")