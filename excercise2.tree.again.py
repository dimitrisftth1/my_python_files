N = int(input("Dwse enan arithmo: "))

for i in range(0,N):
    print(" " * (N-i-1),end="")
    print("*" * (2*i+ 1),end="")
    print("")