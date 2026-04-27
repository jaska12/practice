''' List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enunarate, map and filter
'''

print("===== Working with lists =====")
# Java/PHP/NodeJS array => Python list

#  literal - to'g'ridan qiymat berib yaratish
print("===== Working with lists =====")

person = {"name": "Justin", "age": 25}
people = ("Andrew", "John", "Michael")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]

for team in groups:
    print(f"the team: {team}")

letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")

fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]
c = fruits[:3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("===== List methods =====")

letters = ["a", "d", "b"]

letters.append("c")
letters.insert(0, "z")

letters.pop()
letters.pop(0)

animals = ["dog", "cat", "capybara", "fish", "lion"]
animals.remove("lion")
del animals[2:4]

animals.clear()

numbers = [2, 20, 12, 8, 57]
numbers.sort()
numbers.sort(reverse=True)
print("===== Lambda function =====")


def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]

people.sort()
people.sort(key=lambda person: person[1])
