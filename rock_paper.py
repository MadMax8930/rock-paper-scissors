import random

user_wins = 0
ordi_wins = 0


options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_choice == "q":
        break  #End the program

    if user_choice not in options:
        print("That's is not a valid option")
        continue  #Reask to type the valid option

    randomIndex = random.randint(0,2)  # rock: 0, paper: 1, scissors: 2
    ordi_pick = options[randomIndex]
    print(f"Computer picked {ordi_pick}.")


print("Goodbye!")

