x = int(input("Δώσε τον 1ο ακέραιο: "))
y = int(input("Δώσε τον 2ο ακέραιο: "))
z = int(input("Δώσε τον 3ο ακέραιο: "))

if x > y:
    max = x
else:
    max = y

if max > z:
    print("Ο μεγαλύτερος ακέραιος είναι: " + str(max))
else:
    max = z
    print("Ο μεγαλύτερος ακέραιος είναι: " + str(max))