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


#task 2

def analyze_numbers():
    total = 0
    even = 0
    odd = 0
    total_sum = 0
    while True:
        num = int(input("Enter the number: "))
        
        if num == 0:
            break
        total += 1
        total_sum += num
        
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return total,even,odd,total_sum



total,even,odd,total_sum = analyze_numbers()

print(f"Total numbers are: {total}")
print(f"Total even numbers are: {even}")
print(f"Total odd numbers are: {odd}")
print(f"The total sum of the numbers are: {total_sum}")
            
        
    