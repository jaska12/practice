''' CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("===== Operators =====")
# Arifmetik amallar: +, -, *, /, // (butun bo'lish), % (qoldiq), ** (daraja)

a = 19
b = 5

print(a / b)         # Oddiy bo'lish: 3.8
result = a // b      # Butun qismini olish: 3
left = a % b         # Qoldig'ini olish: 4
print(f"the result: {result} and left: {left}")

# Qisqartirilgan operatorlar
a += 100             # a = a + 100 bilan bir xil
print("a:", a)

# Darajaga ko'tarish
print("b**2", b**2)  # 25
print("b**3", b**3)  # 125

print("-" * 5)       # Matnni ko'paytirish (----- chiqadi)

# Obyektlar va Xotira (Reference)
c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)
e = c

print("c == d", c == d)  # True (qiymatlari bir xil)
print("c is d", c is d)  # False (xotirada boshqa-boshqa joyda)
print("c is e", c is e)  # True (e o'zgaruvchisi c ning manziliga bog'langan)
print(id(c), id(d), id(e))  # Ularning xotiradagi ID manzillari
print("===== Condition =====")
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("===== Logical Operators =====")
age = 21

# person = None
# if age > 16:
#     person = "adult"
# else:
#     person = "minor"
# Ternary operator - bir qatorli shart ifodasi
age = 20
person = "adult" if age > 18 else "minor"
# age 18 dan katta bo'lsa "adult", kichik bo'lsa "minor" qiymat beradi
print("person:", person)  # Natija: person: adult

print("-----")

# Boolean (True/False) o'zgaruvchilar
is_student = True   # Talaba - ha
is_admin = False    # Admin - yo'q
is_guest = True     # Mehmon - ha
is_parent = False   # Ota-ona - yo'q

# Shartli tekshiruv
if not is_student:
    # Agar talaba EMAS bo'lsa
    print("Wellcome here, do you want to be student!")

elif is_admin:
    # Agar admin bo'lsa
    print("Please go to this office!")

elif is_guest or is_parent:
    # Agar mehmon YOKI ota-ona bo'lsa
    print("Waiting room is over there!")

else:
    # Yuqoridagi shartlarning hech biri to'g'ri kelmasa
    print("Other cases")
