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
