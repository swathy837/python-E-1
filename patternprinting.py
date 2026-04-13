N=int(input("Enter no of rows"))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
