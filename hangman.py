import random
words = ["python", "computer", "program", "coding", "developer"]
word = random.choice(words)

guessed = []

attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
   
    count = 0

    for letter in word:
        if letter in guessed:
            count += 1

    if count == len(word):
        print("\nCongratulations! You won!")
        break

    guess = input("Guess a letter: ").lower().strip()
   
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    if guess in guessed:
        print("You already guessed this letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

    print("Attempts left:", attempts)

if attempts == 0:
    print("\nGAME OVER!")
    print("The correct word was:", word)

print("\nThank you for playing!")
