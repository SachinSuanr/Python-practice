#task 1 

num = int(input("Enter the number: "))

if(num % 2 == 0):
    print(f"{num} is an even number.")

else:
    print(f"{num} is an odd number.")
    
    
#task 2 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if(num1 >= num2 and num1 >= num3):
    print(f"{num1} is the largest number.")
elif(num2 >= num1 and num2 >= num3):
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")
    

#task 3
ecount = 0
ocount = 0
while True:
    number = int(input("Enter the number: "))
    
    if(number == 0):
        break
    
    if (number % 2 == 0):
        ecount += 1
    else:
        ocount += 1

print(f"The total even number is {ecount}")
print(f"The total odd number is {ocount}")


#task 4


for i in range(1,5):
    for j in range(1,i+1):
        print(i , end="")
        
        
    print()
    
#task 5 
total = 0
even = 0
odd = 0
sum = 0
largest = None

while True:
    nmb = int(input("Enter the number: "))
    
    
    if(nmb == 0):
        break
    total += 1
    sum += nmb
    
    if (nmb % 2 == 0):
        even += 1
    else:
        odd += 1
        
    if largest is None or nmb > largest:
        largest = nmb
        
print(f"The total number is {total}")
print(f"The total sum is {sum}")
print(f"The even number is {even}")
print(f"The odd is {odd}")
print(f"The largest number is {largest}")