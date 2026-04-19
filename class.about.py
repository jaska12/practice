''' CLASS
(1) What is class
(2) ordinary vs static properties
(3) special methods
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
