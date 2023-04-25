cnt = 0
sum_number = 0

while cnt <= 9 :
    user_number = int(input("Δώστε τον " + str(cnt + 1) + "o ακέραιο αριθμό: "))
    sum_number = sum_number + user_number
    cnt = cnt + 1

print("Το άθροισμα των αριθμών που δώσατε είναι " + str(sum_number))