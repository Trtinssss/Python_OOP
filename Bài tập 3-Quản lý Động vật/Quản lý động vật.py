class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        if self.species == "dog":
            print("Woof!")
        elif self.species == "cat":
            print("Meow!")
        else:
            print("unknown")


animal1 = Animal("lulu", "dog", 3)
animal1.make_sound()
animal1 = Animal("mimi", "cat", 2)
animal1.make_sound()
animal1 = Animal("John", "bird", 3)
animal1.make_sound()