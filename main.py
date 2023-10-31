class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"


dog = Dog("Шарик")
cat = Cat("Барсик")


print(dog.speak())
print(cat.speak())


print(dog.name)
print(cat.name)
