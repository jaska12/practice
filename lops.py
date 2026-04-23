''' LOOP operators
    (1) for
    (2) break/else
    (3) while
'''
# Bu qism ko'p qatorli izoh (docstring) bo'lib, dasturning asosiy mazmunini bildiradi.

print("===== for operator =====")
# Iterable objects > string dict tuple list range map filter
# Bu yerda sikl ishlatish mumkin bo'lgan ma'lumot turlari sanab o'tilgan.

text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)  # [0, 5) gacha bo'lgan sonlar ketma-ketligi

# String (matn) ustida sikl: "M", "I", "T" harflarini bittalab chiqaradi.
for letter in text:
    print(f"the letter: {letter}")

print("-----")
# List (ro'yxat) ustida sikl: ro'yxatdagi har bir sonni chiqaradi.
for number in numbs:
    print(f"the number: {number}")

print("-----")
# Dictionary (lug'at) ustida sikl: har bir kalit (key) orqali uning qiymatini (value) oladi.
for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")


print("===== break/else =====")
# range(1, 20, 5) funksiyasi 1 dan boshlab 20 gacha 5 qadam bilan yuradi (1, 6, 11, 16).
for x in range(1, 20, 5):
    print(f"the x: {x}")
    # Agar x soni 10 dan oshsa, sikl to'xtatiladi.
    if x > 10:
        print("Reached break")
        break
else:
    # else bloki faqat sikl break (to'xtash)siz oxirigacha yetsa ishlaydi.
    # Bu holatda x=11 bo'lganda break ishlagani uchun bu qism ekranga chiqmaydi.
    print("Executed successfully")


print("===== while operator =====")
numb = 40
# numb o'zgaruvchisi 0 dan katta ekan, sikl davom etadi.
while numb > 0:
    numb -= 10  # Har safar 10 ga kamaytiradi.
    print(f"the numb equals {numb}")

print("-----")
count = 0
# while True - bu cheksiz sikl.
while True:
    count += 1  # Urinishlar sonini sanab boradi.
    x = int(input("Find number "))  # Foydalanuvchidan son kiritishni so'raydi.

    # Agar kiritilgan son 41 bo'lsa, g'olib bo'ladi va break orqali sikl to'xtaydi.
    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        # Aks holda qayta so'raydi.
        print("Wrong, please find again!")
