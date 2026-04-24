''' Tuple
    (1) What is tuple: tuple vs list
    (2) Unpacking arguments
    (3) zip
'''

print("===== What is tuple: tuple vs list =====")
# Java/PHP/NodeJS array => Python list (Python'dagi list boshqa tillardagi array'ga o'xshaydi)

# literal - to'g'ridan-to'g'ri ro'yxat yaratish
numbs = [3, 5, 1, 2]

# constructor - list() funksiyasi yordamida ro'yxatga aylantirish
letters = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

# List elementini o'zgartirish mumkin (Mutable)
fruits[2] = "melon"
print("after fruits:", fruits)

# we can not mutate tuple - Tuple elementlarini o'zgartirib bo'lmaydi (Immutable)
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"  # Agar bu qator ishga tushsa, xatolik beradi (TypeError)

# try avoid this - Qavslarsiz ham tuple yaratish mumkin, lekin tavsiya etilmaydi
people = "Alisher", "Jeck"
animals = "dog",  # Bitta elementli tuple yaratish uchun oxirida vergul kerak
print("===== Unpacking arguments =====")
# Ro'yxat elementlarini o'zgaruvchilarga taqsimlash
groups = ["MIT", "ALI", "DEVEX", "MG"]
(x, y, *z) = groups  # x="MIT", y="FLEXY", qolganlari esa z ga list bo'lib yig'iladi
print(f"the x: {x} and y: {y}")
print("z:", z)  # Natija: list ko'rinishida bo'ladi
# **kwargs > dictionary - Kalit so'zli argumentlarni lug'at (dict) qilib yig'ish


def introduce(**kwargs):
    # kwargs - bu funksiya ichida lug'atga aylanadi
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs['name']} and I am {kwargs['age']} years old!")


# CALL - Argumentlar key=value ko'rinishida beriladi
introduce(name="Jeck", age=28)
introduce(name="Alisher", age=30, single=True)
# *args > tuple - Funksiyaga istalgancha oddiy argument uzatish


def calculate(*args):
    print("*args >", args)  # Kelgan barcha sonlar tuple bo'lib tushadi
    total = 1
    for x in args:
        total *= x  # Barcha sonlarni bir-biriga ko'paytiradi
    print(f"the total value: {total}")
    return total


# CALL - Funksiyani turli miqdordagi argumentlar bilan chaqirish
calculate(1, 7, 2, 3)
calculate(0, 2, 300)
calculate(5, 7)
print("-----")

# Ham *args, ham **kwargs ishlatilgan funksiya


def greeting(*args, **kwargs):
    print("*args >", args)      # Oddiy qiymatlar uchun
    print("**kwargs >", kwargs)  # Kalitli qiymatlar uchun


# CALL
greeting("hi", True, 10, name="Jeck", age=22)
print("===== zip =====")
# Ikki to'plamni bir-biriga juftlab birlashtirish
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)  # zip obyekti hosil bo'ladi
print("zipped:", zipped)

# zip natijasini ko'rish uchun uni list'ga o'tkazamiz
result = list(zipped)
# E'tibor bering: tuple2'da 3ta element bo'lgani uchun, natijada ham 3ta juftlik bo'ladi
print(f"the result: {result}")
