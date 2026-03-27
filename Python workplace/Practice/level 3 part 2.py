# 14. Number Guessing Game
# Create a game where:

# Program generates random number (1–100)

# User keeps guessing

# Program says "Too high" / "Too low"

# Stops when correct

# (Hint: use random module)
import random

print("Welcome to the random number guessing system.\n")
def numGuessSys():
    num = random.randint(1, 100)
    return num

g_num = numGuessSys()

while True:
    n = int(input("Guess the number: "))

    if n==g_num:
        print("\nCongratulation! Your guess is correct.\nThe number was: ", g_num)
        break
    elif n>g_num:
        print("Your guess number is 'Too high' compare to the original number.")
    else:
        print("Your guess number is 'Too low' compare to the original number.")