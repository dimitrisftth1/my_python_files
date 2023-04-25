from random import randrange
card_kind = {"heart", "diamond", "spade", "club"}
card_number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}
cards = set()
#dimiourgia trapoulas me 52 fylla
for kind in card_kind:
    for number in card_number:
        card = (number, kind)
        cards.add(card)
print(cards)
print(len(cards))
#orismos paixtwn
player1 = set()
player2 = set()
#moirasma kartwn
list_cards = list(cards)
for _ in range(5):
    pos1 = randrange(0,len(list_cards))
    player1.add(list_cards.pop(pos1))
    pos2 = randrange(0, len(list_cards))
    player2.add(list_cards.pop(pos2))
print(player1)
print(player2)
#kare toy assou
#player1
player1 = {('ace', 'heart'), ('ace', 'club'), ('ace', 'club'), ('ace', 'diamond'), ('ace', 'club')}
cnt = 0
for card in player1:
    if card[0] == "ace":
        cnt += 1
if cnt == 4:
    print("Player1 has kare!!!")
#player2
cnt = 0
for card in player2:
    if card[0] == "ace":
        cnt += 1
if cnt == 4:
    print("Player2 has kare!!!")
#kenta
#player1
hand_numbers = []
for card in player1:
    if card[0] == "ace":
        hand_numbers.append(1)
    elif card[0] == "jack":
        hand_numbers.append(11)
    elif card[0] == "queen":
        hand_numbers.append(12)
    elif card[0] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[0])
hand_numbers.sort()
for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos+1]-1:
        break
    else:
        print("Player1 has Kenta")

#player2
hand_numbers = []
for card in player1:
    if card[0] == "ace":
        hand_numbers.append(1)
    elif card[0] == "jack":
        hand_numbers.append(11)
    elif card[0] == "queen":
        hand_numbers.append(12)
    elif card[0] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[0])
hand_numbers.sort()
for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos+1] - 1:
        break
    else:
        print("Player2 has Kenta")