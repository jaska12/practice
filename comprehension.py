''' Comprehension general syntax:
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version - listni copy qiladi (yangi xotira)

print("list_numbers:", list_numbers)
print(numbers is list_numbers)        # False - ikki xil xotira manzili
print(id(numbers), id(list_numbers))  # har xil id chiqadi


print("------")
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0]
               for person in people]  # b version - faqat ismlarni oladi
print("list_people:", list_people)  # ["Robert", "Steve", "Joseph"]


print("------")
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

# c version - shartga mos elementlarni oladi (tezligi 80 dan katta)
list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars:", list_cars)  # ["Tayota", "Audi", "BMW"]
print("===== set and dictionary comprehension =====")
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}              # takroriy elementlarni o'chiradi
print("set_numbs:", set_numbs)    # {1, 4, 5, 20} - faqat unikal qiymatlar


# dict comprehension - b version
# person[0] = ism (key), person[1] = yosh (value)
dict_people = {person[0]: person[1] for person in people}
print("dict_people:", dict_people)  # {"Robert": 20, "Steve": 19, "Joseph": 25}

# (<expression> for item in iterable) generic
