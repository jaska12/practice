''' CLASS
(1) What is class
(2) ordinary vs static properties
(3) special methods/ magic method ham deb nomlanadi 
'''

print("===== What is class =====")
# class - blueprint for object creation!
# structure > state constructor method


class Person():
    # static state (klassga tegishli xususiyat)
    message = "class state property"

    # constructor (maxsus metod)
    def __init__(self, name, age):
        self.name = name  # ordinary property
        self.age = age   # ordinary property

    # ordinary method (obyektga tegishli metod)
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    # static method (klassga tegishli metod)
    @staticmethod
    def explain():
        print("class: static method property executed!")


# Obyektlarni yaratish (Instances)
person1 = Person("Jeck", 22)
person2 = Person("Jasurbek", 35)
person3 = Person("Javlon", 22)

# Oddiy xususiyatni chiqarish
print("person1.name:", person1.name)

# Metodlarni ishga tushirish
person1.introduce()
person2.say_age()

print("===== ordinary vs static properties =====")

# static state murojaat
new_message = Person.message
print("new_message:", new_message)

# static method murojaat
Person.explain()

print("--- special/magic methods -----")
# Python's most common special methods are below:
# __init__ __name__ __str__ __call__ __getitem__ __add__ __len__ ...


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("* __new__ *")
        # Diqqat: rasmda super().__new__(cls) bo'lishi kerak
        return super().__init__.__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as function!")
        return True


# Obyektlar yaratish va ishlatish
my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("------")
your_car = Car("Tayota", 2026)
print(your_car)  # __str__ metodi ishlaydi
response = your_car()       # __call__ metodi ishlaydi
print("response:", response)
