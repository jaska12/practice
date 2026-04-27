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
print("===== Set =====")
# set → unique collection (takrorlanmaydi, tartib saqlanmaydi)

new_numbers = array("i", [1, 4, 7, 5, 7, 5, 4, 7, 8, 4, 41])
numbs_set = set(new_numbers)  # array → set (duplicate lar o‘chadi)

print(f"the numbs_set: {numbs_set} and type: {type(numbs_set)}")

# yangi element qo‘shadi
numbs_set.add(200)
print("numbs_set(1):", numbs_set)

# 7 bor bo‘lsa ham yana qo‘shilmaydi (set unique)
numbs_set.add(7)
print("numbs_set(2):", numbs_set)


print("===== Specific operators =====")
# a ⊆ b (subset tushunchasi)

a = {10, 20, 50}
b = {20, 40}

# union → hammasini birlashtiradi
result1 = a | b

# intersection → umumiy elementlar
result2 = a & b

# difference → a da bor, b da yo‘q
result3 = a - b

# symmetric difference → faqat farqli elementlar
result4 = a ^ b

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
