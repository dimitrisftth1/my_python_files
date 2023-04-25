array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3] ]
for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")

print("")
array.insert(0, [0, 0, 0, 0])
for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")

for row in array:
    array.append(1)
print("")
#Στο σημείο που προσθέτω τους άσσους μου βγαζει ατερμον δεν ξέρω γιατι
for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")