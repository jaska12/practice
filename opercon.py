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
