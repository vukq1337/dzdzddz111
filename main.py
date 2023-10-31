import random

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 0
        self.energy = 100

    def eat(self, food):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} is eating. Hunger level: {self.hunger}")

    def sleep(self, hours):
        self.energy += hours
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} is sleeping. Energy level: {self.energy}")

    def play(self, time):
        if self.energy < 10:
            print(f"{self.name} is too tired to play.")
        else:
            self.energy -= time
            if self.energy < 0:
                self.energy = 0
            print(f"{self.name} is playing. Energy level: {self.energy}")

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow!")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says Woof!")

class Human:
    def __init__(self, name):
        self.name = name

    def feed(self, animal, food):
        print(f"{self.name} is feeding {animal.name} with {food}.")
        animal.eat(random.randint(5, 15))

    def play_with_animal(self, animal, time):
        print(f"{self.name} is playing with {animal.name}.")
        animal.play(time)

# Приклад використання класів:
if __name__ == "__main__":
    cat = Cat("Whiskers", "Cat")
    dog = Dog("Buddy", "Dog")
    human = Human("Alice")

    for _ in range(3):
        cat.make_sound()
        human.feed(cat, "fish")
        human.play_with_animal(cat, random.randint(10, 30))
        cat.sleep(random.randint(5, 10))

    for _ in range(3):
        dog.make_sound()
        human.feed(dog, "bone")
        human.play_with_animal(dog, random.randint(15, 40))
        dog.sleep(random.randint(6, 12))

    for _ in range(3):
        dog.make_sound()
        dog.eat(random.randint(10, 20))
        dog.play(random.randint(15, 40))
        dog.sleep(random.randint(6, 12))

