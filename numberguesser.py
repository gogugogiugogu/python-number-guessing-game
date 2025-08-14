import random 

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

difficulty = input("Choose a difficulty (easy/hard): ").lower()

if difficulty == "easy":
    attempts = 10 
elif difficulty == "hard":
    attempts = 5  
else:
    print("Invalid choice! I'll set it to easy by default.")
    attempts = 10


secret_number = random.randint(1, 20)

while attempts > 0:
    print(f"\nYou have {attempts} attempts left.")
    
    guess = input("Make a guess: ")
    
    if not guess.isdigit():
        print("Please type a number!")
        continue  

    guess = int(guess)  

    if guess == secret_number:
        print(f"🎉 Correct! The number was {secret_number}. You win!")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")
    
    attempts -= 1

if attempts == 0:
    print(f"😢 Out of attempts! The number was {secret_number}. Better luck next time!")