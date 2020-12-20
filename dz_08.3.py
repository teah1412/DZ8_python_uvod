#Homework 8.3: Calculator

brojA = int(input("Please enter the first number: "))

brojB = int(input("Please enter the second number: "))

operation = input("Which operation do you want to do? Enter +, -, * or /: ")

if operation == "+":
    print(brojA + brojB)

elif operation == "-":
    print(brojA - brojB)

elif operation == "*":
    print(brojA * brojB)

elif operation == "/":
    print(brojA / brojB)

else:
    print("The system does not recognize this operation. Please make sure to not add any spaces before or after the operation sign!")