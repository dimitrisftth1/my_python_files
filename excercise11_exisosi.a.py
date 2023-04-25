a = float(input("Δώσε τον a: "))
b = float(input("Δώσε τον b: "))

if a == 0:
    print("Η εξίσωση δεν έχει λύση!!!")
else:
    x = - a / b
    print("Η λύση της εξίσωσης ax+b=0 είναι: " + str(x))