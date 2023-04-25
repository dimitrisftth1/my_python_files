N = int(input("Δώστε έναν αριθμό μεταξύ 3 και 20: "))
cnt = 0
number_list = []

while N < 3 or N >20:
    print("Λάθος αριθμός !!!")
    N = int(input("Δώστε έναν αριθμό μεταξύ 3 και 20: "))

while cnt < N:
    number = int(input("Δώσε τον " + str(cnt + 1) + " αριθμό:"))
    number_list.append(number)
    cnt = cnt +1

number_list.sort()
print("Η λίστα των αριθμών είναι: \n" + str(number_list))

input('Press Enter to exit')