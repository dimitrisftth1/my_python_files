x1 = int(input("1ος παιχτης 1ο ζάρι: "))
x2 = int(input("1ος παιχτης 2ο ζάρι: "))
y1 = int(input("2ος παιχτης 1ο ζάρι: "))
y2 = int(input("2ος παιχτης 2ο ζάρι: "))

if x1 < 1 or x1 > 6:
    print("Λάθος αριθμός 1ος παίχτης 1ο ζάρι")
elif x2 < 1 or x2 > 6:
    print("Λάθος αριθμός 1ος παίχτης 2ο ζάρι")
elif y1 < 1 or y1 > 6:
    print("Λάθος αριθμός 2ος παίχτης 1ο ζάρι")
elif y2 < 1 or y2 > 6:
    print("Λάθος αριθμός 2ος παίχτης 2ο ζάρι")
elif (x1 + x2) > (y1 + y2):
    print("Ο 1ος παίχτης κερδίζει")
elif (x1 + x2) == (y1 + y2):
    print("Ισοδύναμία, δεν κερδίζει κανένας")
else:
    print("Ο 2ος παίχτης κερδίζει")