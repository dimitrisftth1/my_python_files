prime_list = []

for number in range(2, 100+1):
    for i in range(2,number):
        if number % i == 0:
            break
    else:
        prime_list.append(number)

prime_tuple = tuple(prime_list)
print(prime_tuple)