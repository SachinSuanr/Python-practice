# Day 2 
# Task 1

num = int(input("Enter the number: "))
i = 1

while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i = i + 1



# Task 2 

sum = 0

while True:
    num = int(input("Enter the number: "))
    
    if(num == 0):
        break
    
    sum = sum + num 

print(f"The total sum is: {sum}")

#Task 3

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")

    print()