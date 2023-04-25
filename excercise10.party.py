friends_list = ["a", "b", "c"]
guests_list = ["1", "a", "3", "4", "b", "6", "7", "8", "9", "10"]

friends_in_party = 0

for friends in friends_list:
    for guests in guests_list:
        if friends == guests:
            friends_in_party = friends_in_party + 1

if friends_in_party >= 2:
    print("I'm going to party !!! ")
else:
    print("Sorry I'm not going to party!!!")