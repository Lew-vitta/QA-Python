
n = int(input("enter any number "))
for i in range(1,n+1):    
    for j in range(1,n+1):
        print(i*j, end='\t')
    print("\n")


for row in range(1, n + 1):
    print(*(f"{row*col:3}" for col in range(1, n + 1)))

################################################

count = 0
name = [] 

print("Enter 5 names")
for x in range(5):
    y = str(input(""))
    name.append(y)

while count < 5:
    print(name[count], "is awesome!")
    count += 1   

################################################
#10,12,14,16,18,20
for i in range(10, 21, 2):
    print(i)

