hours = int(input("Δώσε την ώρα: "))
minutes = int(input("Δώσε τα λεπτά: "))
seconds = int(input("Δώσε τα δευτερόλεπτα: "))

if hours < 10:
    message1 = "0" + str(hours)
else:
    message1 = str(hours)

if minutes < 10:
    message2 = "0" + str(minutes)
else:
    message2 = str(minutes)

if seconds < 10:
    message3 = "0" + str(seconds)
else:
    message3 = str(seconds)

message = "Η ώρα είναι, " + message1 + ":" + message2 + ":" + message3
print(message)