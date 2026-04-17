print("===== number =====")

# JAVA tilida o'zgaruvchi - bu qiymat saqlanadigan nomlangan xotira qutisi (location).
# Python tilida esa o'zgaruvchi - bu xotiradagi ob'ektga yo'naltirilgan nom (reference).

count = 100
count_type = type(count)  # O'zgaruvchi turini aniqlaymiz (bu yerda int)

# f-string yordamida o'zgaruvchi qiymati va turini konsolga chiqaramiz
print(f"the count: {count} and type: {count_type}")

# Pythonda hatto sonlar ham ob'ekt bo'lgani uchun ularning o'z metod va xususiyatlari bor:

# 1. bit_count() - sonning ikkilik (binary) ko'rinishidagi 1 lar sonini hisoblaydi
result1 = count.bit_count()  # method

# 2. numerator - butun sonning surati (butun son o'ziga teng)
result2 = count.numerator    # state (xususiyat)

print(result1, result2)

print("===== string =====")
# METODLAR: upper() - hammasini katta, lower() - kichik, title() - har bir so'z bosh harfini katta qiladi,
# find() - qidirish, replace() - almashtirish

course = "AI Python FullStack"
result = type(course)  # O'zgaruvchi turini aniqlaymiz (<class 'str'>)
print(f"the result (1): {result}")

# .title() metodi har bir so'zning birinchi harfini katta qiladi
result = course.title()
print(f"the result (2): {result}")

# .upper() metodi barcha harflarni KATTA harflarga o'zgartiradi
result = course.upper()
print(f"the result (3): {result}")

# .replace() metodi matndagi bir qismni boshqasiga almashtiradi
# Bu yerda "FullStack" so'zi "MasterClass"ga almashmoqda
result = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result}")


print("===== boolean =====")
# Ishlatiladigan funksiyalar: type(), input(), bool(), int(), str()

# 1. Foydalanuvchidan qiymat qabul qilish
y = input("Give your value for y: ")
print("y:", y)

# 2. .isnumeric() metodi kiritilgan matn faqat raqamlardan iboratligini tekshiradi
result = y.isnumeric()
print(f"the input value is numeric: {result}")

# 3. TRUTHY vs FALSY qiymatlar
# Pythonda har qanday ob'ekt mantiqiy (bool) kontekstda True yoki False qiymatga ega bo'ladi.

# TRUTHY (True hisoblanadiganlar): True, noldan farqli sonlar (100, -100), bo'sh bo'lmagan matnlar ("MIT")
# FALSY (False hisoblanadiganlar): False, 0, bo'sh matn (""), None (bo'shlik)

# Barcha Falsy qiymatlarni 'or' orqali tekshirish
test_falsy = "" or False or None or 0
# bool() funksiyasi qiymatni True yoki False-ga o'tkazib beradi
print("test_falsy:", bool(test_falsy))  # Natija: False chiqadi

# Truthy qiymatni tekshirish
test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))  # Natija: True chiqadi
