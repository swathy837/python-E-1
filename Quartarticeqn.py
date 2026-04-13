[25bcs167@mepcolinux ex1.py]$python3 ex1c.py
T=float(input("Enter value of T:"))
S=float(input("Enter value of S:"))
A=float(input("Enter value of A:"))
K=(S*S)-(4*T*A)
if K==0:
    print(-S/(2*T))
    print(-S/(2*T))
    print("The roots are real and equal")
elif K>0:
    print((-S+math.sqrt(K))/(2*T))
    print((-S+math.sqrt(K))/(2*T))
    print("The roots are real and unequal")
else:
    print("The roots are imaginery")
