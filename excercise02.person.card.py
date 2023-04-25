person_card = {}
while True:
    name = input("Δώσε το όνομα του εργαζομένου: ")
    person_card["name"] = name
    surname = input("Δώσε το επίθετο του εργαζομένου: ")
    person_card["surname"] = surname
    father_name = input("Δώσε το πατρώνυμο του εργαζομένου: ")
    person_card["father_name"] = father_name
    birthday = input("Δώσε την ημερομηνία γέννησης του εργαζομένου: ")
    person_card["birthday"] = birthday
    address = input("Δώσε τη διεύθυνση του εργαζομένου: ")
    person_card["address"] = address
    phone = input("Δώσε το τηλέφωνο του εργαζομένου: ")
    person_card["phone"] = phone

    the_end = input("Αν θέλετε να εισαγετε κι άλλον στοιχεία  εργαζομένου πατήστε 'ENTER',  \n "
                    "αν θέλετε να σταματήσετε πατήστε '0': ")
    if the_end == "0":
        print("Ονοματεπώνυμο  : " + person_card["name"] + " " + person_card["surname"] + " του " +
              person_card["father_name"] )
        print("Ημ/νια Γέννησης: " + person_card["birthday"])
        print("Διεύθυνση      : " + person_card["address"])
        print("Τηλέφωνο       : " + person_card["phone"])
        print("Ευχαριστούμε!!!")

        break
    else:
        print("Ονοματεπώνυμο  : " + person_card["name"] + " " + person_card["surname"] + " του " +
              person_card["father_name"])
        print("Ημ/νια Γέννησης: " + person_card["birthday"])
        print("Διεύθυνση      : " + person_card["address"])
        print("Τηλέφωνο       : " + person_card["phone"])
    print("Επόμενη καταχώρηση:")