
def homework_1():
    phone_number= "+62801-0029-9000"
    print("Challenge - Homework 1")
    print("Given this phone number: " + phone_number)
    print("replace “+62” into “0” and omit “-” symbols from the phone number")

    print("Result: " + phone_number.replace("+62", "0").replace("-", ""))
    print()

def homework_2():
    num_list=[12,14,[16,20,30]]
    print("Challenge - Homework 2")
    print("Given this list of number: " + str(num_list))
    print("From the list :\n1. Grab 14\n2. Grab 16, 20, 30\n3. Grab 20")

    print("Result: \n1. " + str(num_list[1]) + "\n2. " + str(num_list[2]) + "\n3. " + str(num_list[2][2]))
    print()

def homework_3():
    numbers=[2,3,6,20,22]
    print("Challenge - Homework 3")
    print("Given this list of number: " + str(numbers))
    print("From the list :\n1. Find the differences between the highest number and lowest number\n2. Get the total value of numbers in list\n3. Grab the 2nd element until the 4th element\n4. Insert new number in the list => number 50")
    appended_numbers = numbers.copy()
    appended_numbers.append(50)

    print("Result: \n1. " + str(max(numbers)-min(numbers)) + "\n2. " + str(sum(numbers)) + "\n3. " + str(numbers[1:4]) + "\n3. " + str(appended_numbers))
    print()

def homework_4():
    print("Challenge - Homework 4")
    print("Create a dictionary containing these key-value:")
    print("'brand'=['Samsung','Dell','Apple']\n'stock'=['27','20'.'10']\n'type'=['PC','Laptop','Tablet']")
    dict = {
        "brand":["Samsung","Dell","Apple"],
        "stock":[27,20,10],
        "type":["PC","Laptop","Tablet"]
    }

    print("Result: " + str(dict))
    print()

def homework_5():
    print("Challenge - Homework 5")
    print("From our existing dictionary (fruits_dic):")
    print("1.Get all of the Quantity value\n2.Get the 2nd element from key ”Color”")
    fruits_dict = {
        "Fruit":["Mango","Banana"],
        "Color":["Blue","Red"],
        "Quantity":[10,25],
    }

    print("Result: \n1. " + str(sum(fruits_dict["Quantity"])) + "\n2. " + fruits_dict["Color"][1])
    print()

def homework_6():
    students = {
        "name":["Budi","Jessica"],
        "age":[19,24],
    }
    print("Challenge - Homework 6")
    print("Given this dictionary:\n" + str(students))
    print("1.Update the value of name into ['Arya','Yusup']\n2.Update age value 19=>22")

    students_result = students.copy()
    students_result["name"] = ["Arya","Yusup"]
    students_result["age"][0] = 22

    print("Result: " + str(students_result))
    print()


def homework_7():
    students = {
        "name":["Budi","Jessica"],
        "age":[19,24],
    }
    print("Challenge - Homework 7")
    print("Given this dictionary:\n" + str(students))
    print("1.Add 'Amar' to the key => name\n2.Add new key and value:\n  'Gender':['Male','Female']")

    students_result = students.copy()
    students_result["name"].append("Amar")
    students_result.update({"Gender":["Male", "Female"]})

    print("Result: " + str(students_result))
    print()

def homework_8():
    students = {
        "name":["Budi","Jessica"],
        "age":[19,24],
    }
    print("Challenge - Homework 8")
    print("Given this dictionary:\n" + str(students))
    print()
    print("1.Delete “Budi” from key=> name\n2.Delete age from the dictionary")

    students_result = students.copy()
    students_result["name"].remove("Budi")
    del students_result["age"]

    print("Result: " + str(students_result))
    print()


homework_list = [
    homework_1,
    homework_2,
    homework_3,
    homework_4,
    homework_5,
    homework_6,
    homework_7,
    homework_8
]

for f in homework_list:
    f()
