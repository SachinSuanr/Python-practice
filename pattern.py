#some pattern question for better understaning of loops (for)
#1
for i in range(5, 0, -1):
    for j in range(1,i*1):
        print(j,end=" ")
        
    print()
    
#2

for i in range(1,7):
    for j in range(1,i*1):
        print(j, end=" ")
        
    print()


#3
for i in range(6,1,-1):
    for j in range(1,i*1):
        print(j,end=" ")
        
    print()
    
#4
for i in range(1,7):
    for j in range(1,i*1):
        print("*", end=" ")
        
    print()



#5

for i in range(1,6):
    for j in range(0 ,i*1):
        print(i, end=" ")
        
    print()
    
#6
for i in range(6,1,-1):
    for j in range(1 ,i*1):
        print("*", end=" ")
        
    print()


#7
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
        
    print()
    