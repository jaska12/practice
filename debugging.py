''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging
'''
# from PIL import Image
from turtle import Screen, Turtle, done
print("===== Python Packages & Core Package =====")
''' Python Packages/Modules: Core, File and External '''
# Core Packages > https://docs.python.org/3/library


# #  Ekran sozlamalari
# screen = Screen()
# screen.bgcolor("white")  # fon rangi oq

# #  Pizza asosi - Turtle obyekti
# pizza = Turtle()
# pizza.speed(2)    # chizish tezligi
# pizza.pensize(2)  # chiziq qalinligi

# #  Doira chizish (pizza asosi)
# pizza.penup()             # qalam ko'taradi
# pizza.goto(0, -150)       # markazga boradi
# pizza.pendown()           # qalam tushiradi
# pizza.color("orange", "yellow")  # chiziq va to'ldirish rangi
# pizza.begin_fill()        # to'ldirishni boshlaydi
# pizza.circle(150)         # radius 150 doira chizadi
# pizza.end_fill()          # to'ldirishni tugatadi

# #  Pizza bo'laklari - 8 ta chiziq
# pizza.color("brown")
# for _ in range(8):
#     pizza.penup()
#     pizza.goto(0, 0)               # markazga qaytadi
#     pizza.setheading(_ * 45)       # 360 / 8 slices = 45° - har bir bo'lak
#     pizza.forward(150)             # oldinga 150 boradi
#     pizza.pendown()                # qalam tushiradi
#     pizza.backward(150)            # orqaga 150 qaytadi


# #  Pepperoni - qizil doira shakllar
# topping = turtle.Turtle()
# topping.shape("circle")   # doira shakl
# topping.color("red")      # qizil rang
# topping.penup()           # iz qoldirmaydi

# #  Pepperoni joylashuvi
# pepperoni_positions = [(-60, 60), (60, 60), (-70, -40),
#                        (70, -40), (0, 90), (0, -80)]
# for pos in pepperoni_positions:
#     topping.goto(pos)   # har bir pozitsiyaga boradi
#     topping.stamp()     # o'sha joyga muhur bosadi

# #  Turtlelarni yashirish
# pizza.hideturtle()
# topping.hideturtle()

# done()  # oynani ochiq ushlab turadi
# Core package
t = turtle.Turtle()
t.shape("turtle")
t.speed(2)
t.circle(150)
turtle.done()


#  Fayl ochish - try/finally usuli
my_file = open("material/message.txt", "r")  # faylni o'qish uchun ochadi
try:
    content = my_file.read()       # fayl ichidagi barcha matnni o'qiydi
    print("content:", content)
finally:
    my_file.close()                # xato bo'lsa ham faylni yopadi


#  Fayl ochish - with usuli (tavsiya etiladi)
# with bloki tugagandan keyin fayl avtomatik yopiladi
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()   # fayl ichidagi matnni o'qiydi
    print("your_content:", your_content)

print("DONE")

print("===== Package Manager & External Package =====")
''' Package Managers: pip pipenv npm yarn composer brew'''
# External Package > https://pypi.org/

# with Image.open("material/logo.png") as img_obj:
#     resized_img = img_obj.resize((200, 200))
#     resized_img.show()
#     resized_img.save("material/sample.png")


print("===== Debugging =====")


def get_summary(*args):  # DEFINE
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount  # find the bug via debugging


test = 100
result = get_summary(1, 2, 3, 4, 5)  # CALL
print("result:", result)
