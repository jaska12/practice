'''
OBJECTS
(1) What is object
(2) Iterable objects & RANGE
(3) DICTIONARY
(4) Error handling system

///
'''

import array   # module (paket ichidagi modul)
import math    # matematik funksiyalar uchun paket
from math import ceil  # faqat ceil funksiyasini alohida import qilyapmiz

print("===== What is object =====")

# Object bu — state (xususiyat) va method (harakat) ga ega bo‘lgan narsa
# Python’da hamma narsa object!

print(type('Hello World!'))  # string object
print(type(100))             # integer object
print(type(True))            # boolean object
print(type(array))           # module object
print(type(math))            # module object

# Paradigm: Functional Programming & OOP
# OOP 4 ta asosiy tushuncha:
# Abstraction | Encapsulation | Inheritance | Polymorphism

result1 = math.ceil(97.7)  # math module orqali ceil chaqirildi
print("result1:", result1)

result2 = ceil(98.7)       # to‘g‘ridan-to‘g‘ri ceil ishlatildi
print("result2:", result2)
