import random
import msvcrt

option = ["Rock", "Paper", "Scissors"]
print()

while True:
    print("⚡ Welcome to the Rock, Paper, Scissors Arena ⚡")
    print("System online. One move. One shot. Outsmart the AI — or be erased from the grid.")
    print()

    print("Input your choice: Rock, Paper, or Scissors. Let’s see if you can outsmart the AI . . .")

    you = input("").capitalize() # Player will type rock/paper/scissors here. Here input are not case sencitive.
    ai = random.choice(option) # AI will pick rock/paper/scissors randomly.
    print()

    print(f"AI choose '{ai}' and you choose '{you}'.")
    print()

    # ------- Game Rules ------- #
    if ai == you:
        print("It's a tie!")
    else:
        if ai == "Rock" and you == "Scissors":
            print("You lose!")
        elif ai == "Scissors" and you == "Rock":
            print("You win!")
        elif ai == "Scissors" and you == "Paper":
            print("You lose!")
        elif ai == "Paper" and you == "Scissors":
            print("You win!")
        elif ai == "Paper" and you == "Rock":
            print("You lose!")
        elif ai == "Rock" and you == "Paper":
            print("You win!")
        else:
            print("Hmm . . . Something went wrong!")

    print()

    # --- Continue or Exit command --- #
    print("Press 'c' to continue or press 'e' to exit...")
    key = msvcrt.getch()
    key_str = key.decode()

    if key_str.lower() == "e":
        print("Exiting...")
        break
    elif key_str.lower() == "c":
        print("Restarting the game...")
        print()
        continue
    else:
        print("Invalid key pressed. Exiting...")
        break
