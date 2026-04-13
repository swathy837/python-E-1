T=input("Enter T(warm/cold):")
H=input("Enter H(dry/humid):")
if T=="warm":
    if H=="dry":
        print("play basketwall")
    elif H=="humid":
        print("Play tennis")
    else:
        print("Invalid choice")
elif T=="cold":
    if H=="dry":
        print("play cricket")
    elif H=="humid":
        print("swimming")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
