import random
game=["rock", "paper", "scissors"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print("User chooses "+game[user_choice])
computer_choice=random.randint(0, 2)
print(f"Computer chooses {game[computer_choice]}")

if user_choice==0 and computer_choice==2:
    print("User Win!")
elif computer_choice==0 and user_choice==2:
    print("User loose!")
elif computer_choice>user_choice:
    print("User loose!")
elif computer_choice==user_choice:
    print("It's a draw!")
else:
    print("User typed an invalid number, you loose!")
