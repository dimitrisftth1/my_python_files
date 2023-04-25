# even 0-100
print("even 0-100")
A = {number for number in range(0,100+1,2)}
print(A)
print(len(A))
# odd 0-100
print("odd 1-100")
B = {number for number in range(1,100+1,2)}
print(B)
print(len(B))
#3 multiples
print("3 multiples")
C = set()
for number in range(0,100+1):
    if number % 3 == 0:
        C.add(number)
print(C)
print(len(C))
#first numbers
print("firsts numbers")
D = set()
for number in range(2, 100+1):
    for i in range(2,number):
        if number % i == 0:
            break
    else:
        D.add(number)
print(D)
print(len(D))
#A|C
E = A | C
print("A|C")
print(E)
F = B & D
print("B&D")
print(F)
F = D & A
print("B&A")
print(F)
print((B|D) and not (B&D))
