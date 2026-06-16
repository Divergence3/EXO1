# guess_number.py

import random

number = random.randint(1, 100)

print("=== GUESS THE NUMBER ===")
print("Devine un nombre entre 1 et 100")

while True:
    guess = int(input("Votre proposition : "))

    if guess < number:
        print("Trop petit")
    elif guess > number:
        print("Trop grand")
    else:
        print("Bravo ! Vous avez trouvé.")
        break
    max_attempts = 10
    