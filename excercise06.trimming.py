while True:
    first_name = input("Give Your  First Name: ")
    first_name.strip()

    if first_name.isalpha():
        first_name = first_name.capitalize()
        break
    else:
        print("YOUR  FIRST NAME PLS!!!")

while True:
    surname = input("Give Your  Surame: ")
    surname.strip()

    if surname.isalpha():
        surname = surname.capitalize()
        break
    else:
        print("YOUR  SURNAME PLS!!!")

print(f"+{28 * '-'}+")
print(f"|{('Hello ' + first_name + ' ' + surname + '!').center(28)}|")
print(f"+{28 * '-'}+")