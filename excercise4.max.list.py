#excercise4
my_list = []
cnt = 0


while cnt <=9:
    number = int(input("Δώσε τον " + str(cnt + 1) + "ο ακέραιο αριθμό: "))
    my_list.append(number)
    cnt = cnt +1

print(my_list)
my_list.sort()

print("Ο μεγαλυτερος απο τους αριθμούς σου είναι: " + str(my_list[9]))