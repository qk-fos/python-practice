import random

rand_num = random.randint(1,9)
guess = 0
count = 0
while (guess != rand_num) and (guess != "exist"):
    guess =  int(input("Guess a number between 1 - 9 : "))
    if guess == "exit":
        break

    count += 1

    if guess < rand_num:
        print(f"{guess} is too low" )
    elif guess > rand_num:
        print(f"{guess} is too high")
    else:
        print(f"Yep! {guess} is the exact number, well done!")

    print(f"{count} guesses so far")