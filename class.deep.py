''' CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("===== ENCAPSULATION =====")


class Account():
    # state -
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        # self.__owner va self.__amount - bular xususiy (private) o'zgaruvchilar.
       # (__) private qiladi .
        self.__owner = owner
        self.__amount = amount

    # method - Klass ichidagi funksiya
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    # Pul kiritish metodi
    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    # Pul yechish metodi
    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner
    # image_39137f.png dagi kod:

    @holder.setter
    def holder(self, new_owner):
        # Bu metod my_account.holder = "JACK" deb yozganingizda ishga tushadi
        print("holder.setter:", new_owner)
        self.__owner = new_owner


# Hisob egasini o'zgartirish uchun maxsus metod

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        # self.__owner - bu xususiy o'zgaruvchi. Unga faqat klass ichidagi
        self.__owner = new_owner


# . Obyekt yaratish:
my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-----")

# 2. Amallar bajarish: Pul qo'shish va yechish
my_account.deposit(3500)   # 3500 qo'shildi
my_account.withdraw(400)   # 400 olindi
my_account.get_balance()  # qoldiqni tekshirish

print("-----")

# 3. MUHIM QISM (Inkapsulyatsiya):
# Quyidagi urinishlar aslida xato berishi yoki ishlamasligi kerak.
# Chunki biz __amount va __owner ni "private" qilganmiz.
# Bu yangi o'zgaruvchi yaratadi, lekin ichki __amount ni o'zgartirmaydi
my_account.amount = 10000000
my_account.owner = "Martin"        # Bu ham ichki __owner ni o'zgartirmaydi
# Natija baribir Shawn va haqiqiy hisobni ko'rsatadi
my_account.get_balance()

print("-----")

# try-except bloki dasturni xatolikni korsatadi
try:
    # __ private bolgani un  ololmaymiz
    result = my_account.__amount
    print("result:", result)

except Exception as err:
    # Agar try bloki ichida xatolik yuz bersa, dastur to'xtamaydi,va  except qismiga o'tadi va xato xabarini chiqaradi.
    print("No target state found:", err)

account_owner = my_account.holder  # state (holat/xususiyat)
print("account_owner:", account_owner)


print("owner before:", my_account.holder)  # state

# change_ownership metodi orqali egasini "JAck"ga o'zgartiramiz
# my_account.change_ownership("JACK")
# print("owner after:", my_account.holder)

my_account.holder = "JASK"
print("owner after:", my_account.holder)
