"""
G-TASK: Integerlardan iborat list qabul qilib, 
uning eng katta qiymatiga tegishli birinchi indexni qaytaradigan funksiya.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) => 1
"""


def get_highest_index(nums):
    # 1. max() funksiyasi orqali ro'yxatdagi eng katta sonni topamiz
    highest_value = max(nums)

    # 2. index() metodi orqali o'sha sonning birinchi uchragan joyini (index) topamiz
    highest_index = nums.index(highest_value)

    # 3. Topilgan indexni natija sifatida qaytaramiz
    return highest_index

# TEKSHIRISH ---


#  21 eng katta, u 1 va 3-indexlarda bor. Funksiya 1 ni qaytarishi kerak.
result1 = get_highest_index([5, 21, 12, 21, 8])
print("Natija 1:", result1)  # 1

# 100 eng katta, u 0-indexda.
result2 = get_highest_index([100, 2, 55, 10, 99])
print("Natija 2:", result2)  # 0

#  9 eng katta, u 4-indexda.
result3 = get_highest_index([1, 2, 3, 4, 9])
print("Natija 3:", result3)  # 4
