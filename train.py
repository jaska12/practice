"""
M-TASK: 
Shart: Shunday function yozing, u string qabul qilsin va string 
palindrom (to'g'ri o'qilganda ham, orqasidan o'qilganda ham 
bir xil o'qiladigan so'z) ekanligini aniqlab boolean qiymat qaytarsin.

MASALAN: palindrom_check("dad") return True; palindrom_check("son") return False;
"""


def palindrom_check(text):
    text = text.lower()
    reversed_text = text[::-1]
    return text == reversed_text

# --- TEKSHIRISH ---


# 1. Palindrom bo'lgan holat
result1 = palindrom_check("dad")
print("result 1:", result1)  # True

# 2. Palindrom bo'lmagan holat
result2 = palindrom_check("son")
print("result 2:", result2)  # False

# 3. Kattaroq palindrom so'z (katta harf bilan)
result3 = palindrom_check("Madam")
print("result 3:", result3)  # True


# """
# K-TASK:
# Shart: Shunday function yozing, u string qabul qilsin va
# string ichidagi eng uzun so'zni qaytarsin.

# MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"
# """


# def find_longest(text):
#     # 1. Stringni .split() metodi orqali bo'shliqlardan ajratib, so'zlar ro'yxatiga o'giramiz
#     words = text.split()

#     # 2. Agar matn bo'sh bo'lsa, None yoki bo'sh string qaytaramiz
#     if not words:
#         return ""

#     # 3. max() funksiyasi yordamida ro'yxatdagi eng uzun so'zni topamiz.
#     # key=len parametri funksiyaga so'zlarning uzunligi bo'yicha solishtirishni aytadi.
#     longest_word = max(words, key=len)

#     return longest_word

# # --- TEKSHIRISH ---


# # 1. Oddiy gap berilgan holat
# result1 = find_longest("I come from Uzbekistan")
# print("result 1:", result1)  # "Uzbekistan"

# # 2. Turli uzunlikdagi so'zlar qatnashgan holat
# result2 = find_longest("Python is an amazing programming language")
# print("result 2:", result2)  # "programming"

# # 3. Faqat bitta so'zdan iborat holat
# result3 = find_longest("Hello")
# print("result 3:", result3)  # "Hello"


# """
# I-TASK:
# Shart: Shunday function tuzing, unga string argument pass bo'lsin.
# Function ushbu argumentdagi raqamlarni (digit) ajratib olib,
# yangi string ko'rinishida return qilsin.

# MASALAN: get_digits("m14i1t") return qiladi "141"
# """


# def get_digits(text):
#     # 1. String ichidagi har bir belgini tekshirib chiqamiz.
#     # 2. .isdigit() metodi yordamida belgi raqam ekanligini aniqlaymiz.
#     # 3. Faqat raqamlarni listga yig'amiz va keyin string holatiga birlashtiramiz.
#     digits = [char for char in text if char.isdigit()]

#     return "".join(digits)

# # --- TEKSHIRISH ---


# # 1. Aralash harf va raqamlar holati
# result1 = get_digits("m14i1t")
# print("result 1:", result1)  # "141"

# # 2. Uzunroq matn va turli belgilar holati
# result2 = get_digits("ad5b8e10")
# print("result 2:", result2)  # "5810"

# # 3. Raqam qatnashmagan holat
# result3 = get_digits("hello world")
# print("result 3:", result3)  # "" (bo'sh string)


# # """
# # G-TASK: Integerlardan iborat list qabul qilib,
# # uning eng katta qiymatiga tegishli birinchi indexni qaytaradigan funksiya.
# # MASALAN: get_highest_index([5, 21, 12, 21, 8]) => 1
# # """


# # def get_highest_index(nums):
# #     # 1. max() funksiyasi orqali ro'yxatdagi eng katta sonni topamiz
# #     highest_value = max(nums)

# #     # 2. index() metodi orqali o'sha sonning birinchi uchragan joyini (index) topamiz
# #     highest_index = nums.index(highest_value)

# #     # 3. Topilgan indexni natija sifatida qaytaramiz
# #     return highest_index

# # # TEKSHIRISH ---


# # #  21 eng katta, u 1 va 3-indexlarda bor. Funksiya 1 ni qaytarishi kerak.
# # result1 = get_highest_index([5, 21, 12, 21, 8])
# # print("Natija 1:", result1)  # 1

# # # 100 eng katta, u 0-indexda.
# # result2 = get_highest_index([100, 2, 55, 10, 99])
# # print("Natija 2:", result2)  # 0

# # #  9 eng katta, u 4-indexda.
# # result3 = get_highest_index([1, 2, 3, 4, 9])
# # print("Natija 3:", result3)  # 4
