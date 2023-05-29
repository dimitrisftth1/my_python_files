from random import randrange

my_words = ["chance",
"faith",
"accumulation",
"architect",
"bathroom",
"count",
"hemisphere",
"press",
"pedestrian",
"kit",
"housewife",
"welfare",
"shock",
"ignorant",
"dramatic"]

guessed_letters = []
cnt = 0
my_number = randrange(0, len(my_words))
hidden_word = my_words[my_number]
#print(hidden_word)

max_rounds = int(input("Give max_rounds: "))

while True:
    cnt += 1
    player_letter = input("\nGive a letter to find the word: ")
    guessed_letters.append(player_letter)
    print(f"The letters you guessed: {guessed_letters} ")
    if player_letter not in hidden_word:
        print(f"The letter {player_letter}, not in word.")
    else:
        print(f"The letter \"{player_letter}\" exist in hidden word {hidden_word.count(player_letter)} times.")

        found = True
        for char in hidden_word:
            if char in guessed_letters:
                print(char, end=" ")
            else:
                print("_", end=" ")
                found = False



        print("")
        if cnt == max_rounds:
            print(f"Sorry lost, the hidden word is, {hidden_word}")
            break
        if found:
            print(f"You found the hidden word '{hidden_word}'")
            break
