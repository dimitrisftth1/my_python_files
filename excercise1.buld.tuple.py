my_list = []
cnt = 1

while cnt <11:
    your_number = int(input("Dwse ton " + str(cnt) + " arithmo apo to 10 ews 20: "))
    if your_number < 10 or your_number > 20:
        print("Lathos Arithmos!!!")
    else:
        my_list.append(your_number)
        cnt += 1

my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)
my_list1 = []

for number in my_list:
    number = number**2
    my_list1.append(number)

my_list1.sort()
my_tuple1 = tuple(my_list1)

print(my_tuple1)