import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = int(input("guess a number between 1 and 9: "))

    if guess == num:
        print("Congratulations! you won!")
        break
    else:
        print("sorry. try again!")