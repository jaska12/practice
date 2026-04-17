# "Dunder" atamasi Double Under (ikki pastki chiziq) so'zidan olingan
# Bu maxsus tizim o'zgaruvchilari va metodlari uchun ishlatiladi

# 1. message nomli o'zgaruvchiga matn (string) qiymatini yuklaymiz
message = "PYTHON: Everything is object!"
print(message)  # Matnni ekranga chiqaramiz

# 2. type() funksiyasi orqali ob'ektning turini (class) aniqlaymiz
# Pythonda har bir ma'lumot (son, matn, ro'yxat) ma'lum bir klassga tegishli ob'ektdir
result = type(message)
print("result:", result)  # Natija: <class 'str'> chiqadi

'''
Pythonda tayyor (built-in) asboblar quyidagi guruhlarga bo'linadi:
(1) TYPES (Turlar) > int (butun son), float (o'nlik), str (matn), list (ro'yxat), dict (lug'at)
(2) FUNCTIONS (Funksiyalar) > print(), len() - uzunlik, input() - kiritish, type() - turini aniqlash
(3) CONSTANTS (O'zgarmaslar) > True (to'g'ri), False (notog'ri), None (bo'sh qiymat)
'''

# 3. __builtins__ bu Pythonning ichki "asboblar qutisi" hisoblanadi.
# dir() funksiyasi bu quti ichida qanday tayyor funksiyalar va o'zgarmaslar borligini
# ro'yxat ko'rinishida chiqarib beradi.
print(dir(__builtins__))
