name=input("Enter your name: ")
nameLength = len(name)

for i in range(0, nameLength):
    for j in range(0, nameLength):
        if(i==j):
            print(name[j], end=" ")
        else:
            print("*", end=" ")
    print()
