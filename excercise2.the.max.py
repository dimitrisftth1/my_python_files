list_int = [4, 23, 17]
print(list_int)

maximum = list_int[0]

if maximum < list_int[1]:
    maximum = list_int[1]
if maximum < list_int[2]:
    maximum = list_int[2]

print(maximum)
