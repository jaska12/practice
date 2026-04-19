''' CLASS
(1) What is class
(2) ordinary vs static properties
(3) special methods
'''

print("===== What is class =====")
# class - blueprint for object creation! (obyekt yaratish uchun qolip)
# structure > state constructor method (tuzilishi: holat, konstruktor va metod)


class Person():
    # state (holat yoki klass xususiyati)
    message = "class state property"

    # constructor (konstruktor)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method (metod - klass ichidagi funksiya)
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")


# Obyektlarni yaratish (Instances)
person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# Oddiy xususiyatni chiqarish
print("person1.name:", person1.name)

# Metodlarni ishga tushirish
person1.introduce()
person2.say_age()
