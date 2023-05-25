import random
Heads = 0
Tails = 1

game_on = True
while game_on:
    print("Welcome to Heads or Tails!")
    coin_toss = random.randint(0, 1)
    decision = input("Please select an option, Heads or Tails: ")

    if decision == 'Heads':
        if coin_toss == Heads:
            print("Congratulations, you are correct!")
        elif coin_toss == Tails:
            print("You are not correct. Game Over")
    elif decision == 'Tails':
        if coin_toss == Tails:
            print("Congratulations, you are correct!")
        elif coin_toss == Heads:
            print("You are not correct, it was Tails. Game Over")
    else:
        print("Invalid answer. Please input Heads or Tails")

    game_decision = input("Do you want to keep playing?: Y/N ")

    if game_decision == 'Y' or game_decision == 'y':
        game_on = True
    else:
        game_on = False
        print("Thanks for playing!")
        break