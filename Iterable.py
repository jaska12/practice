print("===== Iterable objects & RANGE =====")
# Iterable obyektlar: string, dict, tuple, list, range, map, filter

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")


print("===== DICTIONARY =====")
# Dictionary (Lug'at) JSON obyektiga o'xshash tuzilishga ega
person = {"name": "JACK", "age": 25, "single": True}
person_obj = dict(name="JACK", age=25, single=True)

print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# get() metodi bilan ishlash
# name = person_obj["name"]  <-- Bu usulda kalit topilmasa xato beradi
name = person_obj.get("name")
hobby = person_obj.get("hobby")  # Kalit topilmasa None qaytaradi
balance = person_obj.get("balance", 0)  # Kalit topilmasa 0 qaytaradi

print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

# Ma'lumotni o'chirish
del person_obj["single"]

# Lug'at bo'ylab aylanish (loop)
for key in person_obj:
    print(f"the key: {key} > value {person_obj.get(key)}")
