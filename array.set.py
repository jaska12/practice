''' Array & Set
    (1) Array
    (2) Set
    (3) Specific operators with set
'''

# array modulidan array classni import qilyapmiz
from array import array
print("======== Array =======")

# 'i' → integer tipdagi array (faqat butun sonlar)
numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)  # boshlang‘ich array

# oxiriga element qo‘shadi
numbers.append(100)

# index bo‘yicha qo‘shadi (0-index ga 14 qo‘shadi)
numbers.insert(0, 14)
print("numbers(2):", numbers)

# qiymat bo‘yicha o‘chiradi (5 ni o‘chiradi)
numbers.remove(5)

# oxirgi elementni olib tashlaydi
numbers.pop()
print("numbers(3):", numbers)

# 0 dan 2 gacha bo‘lgan elementlarni o‘chiradi
del numbers[0:2]
print("numbers(4):", numbers)
