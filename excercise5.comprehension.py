my_list = []
for number in range(100):
    if number % 2 == 0 and number % 3 == 0:
        my_list.append(number)
print(my_list)

#list comprehension
my_list = [number for number in range(100) if number%2==0 and number%3==0]
print(my_list)