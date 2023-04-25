active = True

while active:
    user_input = input("Δώσε έναν αριθμό ή 'quit': ")

    if user_input == "quit":
        print("Τέλος προγράμματος !!!")
        active = False
    else:
        number_input = int(user_input)
        number = number_input ** 2
        print("Το τετράγωνο του αριθμού " + str(number_input) + " είναι ο " + str(number))