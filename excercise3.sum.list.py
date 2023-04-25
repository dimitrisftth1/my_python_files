cnt = 0
my_list = []
sum = 0

while cnt <= 9:
    number = int(input("Δώσε τον " + str(cnt + 1) + "ο αριθμό: "))
    my_list.append(number)
    sum = sum + number
    cnt = cnt + 1

print("Οι αριθμού που δώσατε έιναι: " + str(my_list))
print("Το άθροισμα των αριθμών σας είναι: " + str(sum))