cash_desk = []
print(cash_desk)

print("Πρόσθεσε στην ουρά τον Tom")
cash_desk.append("Tom")
print(cash_desk)

print("Πρόσθεσε στην ουρά τον Bob")
cash_desk.append("Bob")
print(cash_desk)

print("Αφαίρεση του 1ου ατόμου της ουράς")
customer0 = cash_desk.pop(0)
print("Ο πελάτης " + customer0 + " εξυπηρετήθηκε")

print("Πρόσθεσε στην ουρά την Pam και τον Jim και τυπωσέ την ουρά")
cash_desk.append("Pam")
cash_desk.append("Jim")
print(cash_desk[-1])
print(cash_desk)

print("Αφαίρεσαι το 1ο άτομο της ουράς και τύπωσε ότι εξυπηρετήθηκε")
customer0 = cash_desk.pop(0)
print("Ο πελάτης " + customer0 + " εξυπηρετήθηκε")
print(cash_desk)

