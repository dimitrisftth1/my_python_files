hidden = [1, 2, 1, 3, 4, 2, 4, 3]
N = 8
state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]
#other states: open, temp_open
active_game = True
found = 0
score = 0
#give first position
while active_game:
    score += 1
    # read first position
    first_position = int(input("Give first position  (0 - " + str(N-1) + ") and closed: "))
    while first_position < 0 or first_position > 7:
        print("Error!!!")
        first_position = int(input("Give first position  (0 - " + str(N - 1) + ") and closed: "))
    #read second position
    second_position = int(input("Give second position  (0 - " + str(N - 1) + ") and closed: "))
    while (second_position < 0 or second_position > 7) or first_position == second_position:
        print("Error!!!")
        second_position = int(input("Give second position  (0 - " + str(N - 1) + ") and closed: "))
    #change state: both temp_open
    state[first_position] = "temp_open"
    state[second_position] = "temp_open"
    #print current station
    print("")
    for position in range(N):
        if state[position] == "closed":
            print("_", end=" ")
        elif state[position] == "open":
            print(hidden[position], end=" ")
        else: #state[position] == "temp_open
            print(hidden[position], end=" ")
    print("")
    #check if same then open else closed
    if hidden[first_position] == hidden[second_position]:
        state[first_position] = "open"
        state[second_position] = "open"
        found += 2
        if found == N:
            print("Bravo!!! Game finished and your score is " + str(score))
            active_game = False
        print("Success!!!")
    else:
        state[first_position] = "closed"
        state[second_position] = "closed"
        print("Failure!!!")
        print("")
        for position in range(N):
            if state[position] == "closed":
                print("_", end=" ")
            elif state[position] == "open":
                print(hidden[position], end=" ")
            else:  # state[position] == "temp_open
                print(hidden[position], end=" ")
        print("")

