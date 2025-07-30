import random

secret_num = random.randint(1,100)
attempts =10


print("Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it.\n")

for attempts in range(1, attempts+1):
      guess = int(input(f"Attempt {attempts} - Enter your guess: "))
      if guess == secret_num:
            print("Congratulations you have guessed the correct number! ")
            break
      elif guess < secret_num:
        print("Too low. Try again.")
      else: 
        print("Too high. Try again.")

      
else:
        print(f"\n Out of attempts! The number was {secret_num}. Better luck next time!")