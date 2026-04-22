''' CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("===== INHERITENCE =====")
# OTA KLASS


class Animal:  # Parent
    # state
    description = "The class creates animals"

    # constructor
    def __init__(self, voice):
        self.voice = voice
        self.status = "animal is alive"

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


# BOLA KLASS - DOG (Animaldan meros olgan)
class Dog(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        # super() orqali ota klassning constructoriga voice yuboriladi
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


# BOLA KLASS - CAT (Animaldan meros olgan)
class Cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


# BOLA KLASS - FISH (Animaldan meros olgan)
class Fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "Zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("------")
dog.make_voice()
fish.make_voice()

print("------")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("status:", dog.status)
