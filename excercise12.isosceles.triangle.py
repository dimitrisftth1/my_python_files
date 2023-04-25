N = int(input("Dwse arithmo grammon: "))
while N<0:
    N = int(input("Dwse arithmo grammon: "))
else:
    for i in range(0,N):
        for j in range(0,N-i-1):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        print("")