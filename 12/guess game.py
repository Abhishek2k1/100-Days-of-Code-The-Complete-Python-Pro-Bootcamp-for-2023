#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")
difficulty=input("Coose a difficulety. Type 'easy' or 'hard'")
attempts=0
if(difficulty=="easy"):
    attempts=10
elif(difficulty=="hard"):
    attempts=5
else: 
    print("Invalid difficulty level selected")

number=random.randint(1,101)
# print({attempts})
print({number})

while(attempts>0):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: \n"))
    if(number<guess):
        print("Too high\nGuess again")
    elif(number>guess):
        print("Too low\nGuess again")
    elif(number==guess):
        print(f"You got it! The answer was {number}")
        exit()
    attempts=attempts-1

print(f"you have exhausted your attempts. The answer was {number}")