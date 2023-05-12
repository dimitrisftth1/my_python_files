quote = "I don't hate them...I just feel better when they're not around."

while True:
    my_word = input("Give a word: ")
    my_word = my_word.strip()

    if my_word == "quit":
        break

    if quote.find(my_word) != -1:
        print(quote.replace(my_word,my_word.upper()))
    else:
        print("Didn't find !")






