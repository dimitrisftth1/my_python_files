print("Άρτιοι αριθμοί από 10 εώς 20")
for number in range(10,20+1,2):
    print(number)

print("Περιττοί αριθμοί από 19 εώς το 11 φθίνουσα σειρά")
for number in range(19,11-1,-2):
    print(number)

print("περιττοί αριθμοί από 1 εως το 29 πολλαπλάσια του 3")
for number in range(1,29+1,2):
    if number%3 == 0:
        print(number)