"""
TÄIENDUSED
    1. when game over, ask retry?
"""


from random import randint

steps = 0

def ask():
    global steps, game_over, pc_nr
    user_nr = int(input("Number: "))

    steps += 1

    if user_nr > pc_nr and user_nr != -1337:
        print("Lower")
    elif user_nr < pc_nr and user_nr != -1337:
        print("Higher")
    elif user_nr == pc_nr or user_nr == -1337:
        print(f"YOU WIN! number was {str(pc_nr)}, steps: {steps}"); game_over = True
    else:
        print("INVALID")
    return user_nr

def game():
    global steps, pc_nr, game_over
    while True:
        pc_nr = randint(1, 100)
        steps = 0
        game_over = False
        while not game_over:
            unr = ask()
        retry = input("retry? (y/n): ")
        if retry == "n":
            if unr != -1337:
                print(f"Save to leaderboard? steps: {steps}")
                name = input("Name: ")
                with open("results.txt", "a") as f:
                    f.write(f"\n{name}: {unr}")
                    f.close()
                print("Saved.")
                with open("results.txt", "r") as f:
                    lead = f.readlines()
                    print("\nCurrent leaderboard:\n")
                    print(lead)
                    f.close()
                exit()



game()
