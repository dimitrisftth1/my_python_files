N = 5
my_set = {number for number in range(N)}
print(my_set)
set_square = set()
for number in range(N):
    num_square = number**2
    tuple_square = (number,num_square)
    set_square.add(tuple_square)
print(set_square)
