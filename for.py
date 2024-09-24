#knowing the for statement by Brandon Barber
###   3.23.24

'''mood = input("Hey Brandon this is Sonic how are you! ")
print("Nice! im" ,mood,"too just running in green hill zone! Its very nice out here! im about to hit up a chilli dog "
                      "suprsingly with Robonik!")
q2 = "on a scale 1- 100 rings how much you bet its a trap?"
rating = eval(input(q2))
print("Yeah i had a feeling. I already doged a badnick' ) '''

#### commenting all at the same time  = ctrl+/
#or you can use ( ''' ''' )###

'''making a taple  this the "*" sign'''
'''def make_pizza(*topping):
    print(topping)

make_pizza('me',"you","myslelf")'''


'''name = ["cloud","barret","tifa"]
list = "%s , %s , %s"
print(list % (*name,))'''

# name = ["cloud","barret","tifa"]
# list = "%s , %s , %s"
# print(list % tuple(name))


'''import math
from math import sqrt


print("the square root 25 is",sqrt(25))
print("the log10 of 100 is", math.log10(100))
print("tha absolute value of 25 is", abs(25))

phrase = "This is python!!"
print(phrase.upper())
print(phrase.lower())
print(phrase.lower().isupper())
print(phrase.lower().islower())
print(phrase.count("s")) #count element of a string exp there are 2 "i" in  "this is python"
print(phrase.isdecimal())'''
# print()
# for i in range(1,6): #start stop
#     print(i)
#
# print()
#
# for i in range(2,12,3):   #start,stop,step
#     print(i)
#
# print()
#
# for hours in range(-10,1,2):
#     print(hours,end="") # can put anything at the end of every value
# print()
# print()
#
# for i in range (4):
#     print("****")
# print()
# for i in range(4):
#     print("*"*4)
# print()
#
# for i in range(4):
#     for j in range(4):
#         print("*",end= "")
#     print()
# print()
# print()
# for i in "****":
#     print("****")
# print()
#
#
# for i in "csci 150":
#     print(i)
# print()
#
# for i in range(1,11):
#     print(i)


# for i in range(10,26,5):
#     print(i, end=" ")
#
# print(i+ 5)
#
# for i in range(-3,21,3):
#     print(i,end = ",")
# print(i+3)
#
# print()
#
# s = 0
# for i in range(10):
#     num = float(input("Enter a number:"))
#     s += num
#
# print("average number is:", s / 10)

# list = [1,2,3,4,5,6,7,8,9,10 ]
# list.reverse()
# print(list, "HAPPY NEW YEAR!!!")
#

# x = 3
# y = 7
#
# print ( not x  == 5)
# print (x > 0 and y > 0)
# print (not (x == 0 or y == 5))
# print (not y == 0 or x == 10)
# print (not x == "not even strings in here")

# import turtle
#
# def square(len):
#     for i in range(4):
#         turtle.forward(len)
#         turtle.right(90)
#
# def house(zen):
#     square(zen)
#     triangle(zen)
#
# def triangle(ben):
#     for i in range(3):
#         turtle.forward(ben)
#         turtle.left(120)
#
'''def basic_moves():
        x += 1 
        y -= 1
# special_move

# def main(): could be called anything besides main() could be world() or zone()
#     turtle.color("blue")
#     turtle.speed(2)
#     house(100)
#     turtle.color("orange")
#     turtle.penup()
#     turtle.forward(150)
#     turtle.pendown()
#     house(50)
#     turtle.color("purple")
#     turtle.penup()
#     turtle.backward(255)
#     turtle.pendown()
#     house(50)
#
  square(50) #len moves at 50 pixels
#     triangle(100) # ben is moving 100 pixels
#     zen moves both len and ben at 100 then 50 pixles'''
#
# main()
# turtle.Screen().exitonclick()
#
# import random
#
# random_number = random.randint(1,1000)
#
# def  add(x,y):
#    return x + y
#
# def multiply(x,y):
#     return x * y
#
#
# a = eval(input("give me number:"))
# b = eval(input('give me number:'))
#
# print("Sum:",add(a,b), "product:",multiply(a,b))
# print(random_number)

'''
print("*" * 55)
print("!","Car wash fundraiser for April fool to you Do Thuy","!")
print("*" * 55)
'''
'''
phrase = "hELlo glO"

print(phrase.lower())
print(phrase.title())
print("hello glc")
print(phrase.upper())
print(phrase)
'''

'''
for i in range(50):
    print("HELLO GLC".title())
'''
'''
for i in range(1,11):
    print("%" * i)
'''
'''
j = 77
while j >= -77:
    print(j)
    j -= 1
'''

# 1string = "Hello"
# builder = " "
# i = 0
# while i < len(string):
#  builder += string[i].swapcase()
#  print(i, builder)
#  i += 1
# print(string, "->", builder)

# x = 0
# i = 1
# while x < 20:
#     if x > 5:
#      x += 15
#     else:
#      x += 1
#      print(i, x)
#      i += 1



'''for i in range(10):
    print(i)
'''
'''
a = "viruses"
b= 1
while b > 0:
    print(a)
'''
'''
for i in range(1,10):
    if is_even(i):
        print(i)
'''
'''
import turtle

def draw_arc(t, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    for _ in range(180):
        t.forward(radius * 0.01745)  # Approximation for small steps
        t.right(1)

def create_turtle(t, color, width):
    t.shape("turtle")
    t.color(color)
    t.speed(15)
    t.width(width)

def draw_rainbow():
    colorsList = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    radius = 450
    width = 25
    for i, color in enumerate(colorsList):
        t = turtle.Turtle()
        create_turtle(t, color, width)
        draw_arc(t, radius, -radius + width * i, -175)
        radius -= width

    # Hide all the turtles after drawing
    for t in turtle.turtles():
        t.hideturtle()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Draw the rainbow
draw_rainbow()

turtle.done()
'''
'''
shopping_list = {
    fruits: [apple","banana", "orange"],
    vegetables: [carrot", "broccoli", "spinach"], 
    dairy: ["milk", "cheese", "yogurt"],
    meat: ["chicken", "beef", "pork"],
    grains: ["rice", "pasta", "bread"]
    }

print(shopping_list)

'''
#
# x = 5
# while x > 0:
#     print(x)
#     x -= 1


# def calculate_sum(n):
#     sum = 0
#     for i in range(n):
#         if i % 2 == 0:
#             sum += i
#     return sum
#
# result = calculate_sum(10)
#
# print(result)

# def print_numbers(start, end):
#     for num in range(start, end + 3):
#         if num % 2 == 0:
#             print(num, end=' ')
#
# print_numbers(1, 10)

# def multiply_numbers(a, b):
#     return a * b
#
# result = multiply_numbers(3, 4) + multiply_numbers(2, 5)
# print(result)
# print(12 + 10)
#
# def calculate_average(numbers):
#     sum = 0
#     count = 0
#     for num in numbers:
#         sum += num
#         count += 1
#     average = sum / count
#     return average
#
# scores = [85, 92, 78, 90, 88]
# result = calculate_average(scores)
#
# if result >= 80:
#     print("Congratulations! You passed.")
# else:
#     print("Sorry, you failed.")

# for i in range(3):
#     for j in range(2):
#         print(i,j)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# result = factorial(5)
#
# print(result)
#
# for lo in range(7,-7,3):
#     print(lo)
'''


