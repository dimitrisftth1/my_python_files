a = int(input("Δώσε τον 1ο ακέραιο: "))
b = int(input("Δώσε τον 2ο ακέραιο: "))
c = int(input("Δώσε τον 3ο ακέραιο: "))

if a > b and a > c:
    Max = a
elif b > a and b > c:
    Max = b
else:
    Max = c
print("Ο μεγαλύτερος αριθμός είναι: " + str(Max))