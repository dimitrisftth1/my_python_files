stack = []
print(stack)

print("Αίτημα Bob και john")
request = ["Bob", "John"]
stack.extend(request)
print(stack)

print("Εξυπηρέτηση του τελευταίου αιτήματος")
last_request = stack.pop()
print("O " + last_request + " εξυπηρετήθηκε")

print("Αίτημα της Pat")
stack.append("Pat")
print(stack)