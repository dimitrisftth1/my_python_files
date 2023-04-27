from random import randrange
cnt = 0
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
number_of_dice = int(input("Γράψε, Πόσες ζαριές θα ρίξεις: "))
while number_of_dice < 0:
    number_of_dice = int(input("Γράψε, Πόσες ζαριές θα ρίξεις: "))


while True:
    roll = randrange(1, 7)
    for key in dice.keys():
        if roll == key:
            dice[key] += 1
            cnt += 1
    if cnt == number_of_dice:
        break
print(dice)

for key, value in dice.items():
    rol1 = (key, (value/ number_of_dice) * 100)
    print("Το ποσοστό απο τη ζαριά Νο:" + str(rol1) + "%")