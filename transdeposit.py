B=float(input("Enter initial amount balance"))
T=input("Enter transaction type(deposit/withdrawal):")
if T=="deposit":
    A=float(input("Enter deposited amount:"))
    if A>=100:
        print("Balance:",A+B)
    else:
        print("Your amount is not sufficient for deposit")
elif T=="withdrawal":
    C=float(input("Enter withdrawal amount:"))
    Balance=B-C
    if B<=1000:
        print("Your balance should be at least 1000...so pls withdraw accordingly")
    else:
        print("Balance:",B-C)
