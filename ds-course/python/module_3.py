import math

def homework_1():
    numbers=[4,5,10,20,40,60,80]
    print("Challenge - Homework 1")
    print("Given this list of numbers: " + str(numbers))
    print("Create new list called “new_list” containing all number higher than 10")

    new_list = []
    for n in numbers:
        if n > 10:
            new_list.append(n)


    print("Result: " + str(new_list))
    print()

def homework_2():
    def circle_area(r):
        print(math.pi * r ** 2)
        # return math.pi * r ** 2
         
    print("Result: ")
    circle_area(10)
    print()

def homework_3():
    def two_numbers(a,b):
        print(a + b)
        print(a * b)
        print(a if a >= b else b)

         
    print("Result: ")
    two_numbers(11, 12)
    print()

homework_list = [
    homework_1,
    homework_2,
    homework_3,
]

for f in homework_list:
    f()
