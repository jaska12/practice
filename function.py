'''
FUNCTIONS
(1) DEFINE vs CALL (Aniqlash va Chaqirish)
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope (Ko'rinish sohasi)
'''

print("===== DEFINE (PARAMETER) vs CALL (ARGUMENT)=====")
# build in function (tayyor funksiyalar) > print() type()
# Function - reusable block of code! (Funksiya - qayta ishlatiladigan kod bloki)
# Java-dagi {} qavslar o'rniga Python-da surish (indentation) ishlatiladi!

# 1. DEFINE (Funksiyani qurish/yaratish)   PARAMETER


def greet(a):
    # Bu funksiya shunchaki ma'lumotni ekranga chiqaradi (print)
    print(f"How do you do, {a}")


def greeting(b):
    # Bu funksiya esa natijani qaytaradi (return)
    print("greeting is executed")
    return f"Hi {b}"


# 2. CALL (Funksiyani ishga tushirish/chaqirish)excute                 ARGUMENT
# greet() funksiyasini chaqiramiz. U ichida 'return' bo'lmagani uchun None qaytaradi.
result1 = greet('Jasurbek')
# result1: None chiqadi, chunki greet funksiyasida return yo'q
print("result1:", result1)

result2 = greet('jack')
print("result2:", result2)
# jacek


print("===== Keyword & default arguments =====")

# DEFINE - Funksiyani yaratish
# age=22 bu "Default argument" hisoblanadi.
# Agar funksiya chaqirilganda yosh berilmasa, avtomatik 22 olinadi.


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"

# CALL - Funksiyani chaqirish


# 1. Keyword arguments (Kalit so'zli argumentlar)
# Bu usulda biz argumentlarni nomi bilan uzatamiz: name="Justin", age=28
# Bunda argumentlar ketma-ketligini almashtirib yozsa ham bo'ladi.
result3 = give_greet(name="jack", age=28)
print("result3:", result3)

# 2. Default value ishlatilishi
# Biz faqat "John" ismini berdik, age (yosh) uchun qiymat bermadik.
# Shunda funksiya o'zining tepada belgilangan age=22 qiymatini ishlatadi.
result4 = give_greet("jack")
print("result4:", result4)
