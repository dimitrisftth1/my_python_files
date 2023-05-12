string = """
How the hell could a person enjoy being awakened at 6:30AM, 
by an alarm clock, leap out of bed, dress, force-feed, shit, piss, 
brush teeth and hair, and fight traffic to get to a place 
where essentially you made lots of money for somebody else 
and were asked to be grateful for the opportunity to do so?"""

string = string.lower()

letters = set(string)
#print(letters)
dictionary_string = {letter: 0 for letter in letters }
print(dictionary_string)

for char in string:
    dictionary_string[char] += 1

for char in " ,\n-:036?":
    dictionary_string.pop(char)


for key in sorted(dictionary_string.keys()):
    print(f"{key}: {dictionary_string[key]}")