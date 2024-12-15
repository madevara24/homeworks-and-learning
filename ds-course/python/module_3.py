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


def homework_4():
    customer_name = input("Please input your name: ")
    menus = {
        "Latte": 23000,
        "Americano": 21000,
        "Espresso": 18000,
        "Donut": 9000,
        "Croffle": 20000
    }

    order_list = {}
    total_price = 0
    while True:
        print("\nHello " + customer_name + ", here's our menu for today:")
        for menu_item in menus:
            print(f"{menu_item:<15} Rp.{menus[menu_item]:>8}")
        item = input("Enter the menu to add\nEnter n to finish\nEnter your order:").lower()
        
        if item == 'n':
            break
            
        if item in menus:
            if item in order_list:
                order_list[item] += 1
            else:
                order_list[item] = 1  
            print(item + " added")
        else:
            print("Sorry, that's not available")
            
    print("\nYour order contains:")
    for item, quantity in order_list.items():
        item_total = menus[item] * quantity
        total_price += item_total
        print(item)
        formated_quantity_price = str(quantity) + " x IDR " + str(menus[item])
        formated_item_total = "IDR " + str(item_total)
        print(f"{formated_quantity_price:<14} {formated_item_total:>10}")

    formated_total = "IDR " + str(total_price)
    print(f"\nTotal: {formated_total:>18}")

homework_list = [
    homework_1,
    homework_2,
    homework_3,
    homework_4
]

for f in homework_list:
    f()
