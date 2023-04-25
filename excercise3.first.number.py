my_number = int(input("Dwse enan arithmo >=2: "))

while my_number <2:
    print("Lathos arithmos!")
    my_number = int(input("Dwse enan arithmo >=2: "))
else:
    for number in range(2,my_number):
        if my_number % number == 0:
            print("It's not prime!!!")
            break
    else:
        print("It's prime!!!")