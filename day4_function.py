# function

#task 1

def add(a, b):
    return a+b
    
def subtract(a ,b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a/b
    

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The sum of numbers is:{add(num1,num2)}")
print(f"The difference of numbers is: {subtract(num1,num2)}")
print(f"The multiplication of numbers is: {multiply(num1,num2)}")
print(f"The division of numbers is: {divide(num1,num2)}")