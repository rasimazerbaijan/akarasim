balance=500
while True:
    op=input("widraw or deposit w or p: ")
    summm=int(input())
    if op=="w":
        if summm>balance:
            print("can ay kasib")
        else:
            balance-=summm
    else:
        balance+=summm
    print(balance)

