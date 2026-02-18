import math
#Task 1
print("1.Personal Info of the user.....")

name = input("Enter the user name: ")
age = int(input("Enter the age of user: "))
college = input("Enter the college of user: ")

print(f"Name is: {name}")
print(f"The age is: {age}")
print(f"The college name is: {college}")

#Task 2
print("2.Simple Calculator")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

if (operator == "+"):
    print(f"The addition of numbers is: {num1 + num2}")
elif (operator == "-"):
    print(f"The subtraction of numbers is: {num1 - num2}")
elif (operator == "*"):
    print(f"The multiplication of numbers is: {num1 * num2}")
elif (operator == "/"):
    if(operator != 0):
        print(f"The division of the numbers is: {num1 / num2}")
    else:
        print("Division is not possible")
else:
    print("Invalid operator")
    
#Task 3
r = int(input("Enter the radius of the circle: "))

area = math.pi * r**2

print(f"The area of the circle is: {area}")