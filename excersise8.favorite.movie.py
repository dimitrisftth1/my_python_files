#mov1 = input("Γράψε την 1η αγαπημένη ταινία: ")
#mov2 = input("Γράψε την 2η αγαπημένη ταινία: ")
#mov3 = input("Γράψε την 3η αγαπημένη ταινία: ")
#mov4 = input("Γράψε την 4η αγαπημένη ταινία: ")

#my_movies_list = [mov1, mov2, mov3, mov4]

my_movies_list = ["Σ'αγαπώ", "Πατριώτης", "Οι Λίζα και οι άλλοι", "Τιτανικός"]

movie = input("Δώσε μια αγαπημένη ταινία: ")

if movie in my_movies_list:
    print("Η ταινία που γράψατε υπάρχει ήδη!!!")
else:
    my_movies_list.append(movie)
    my_movies_list.sort()
    print(my_movies_list)