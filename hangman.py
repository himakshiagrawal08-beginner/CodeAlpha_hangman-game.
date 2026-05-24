import random

print("===================================")
print("🎮 Welcome to Hangman Game 🎮")
print("===================================")

words = ["apple", "tiger", "parrot", "queen", "banana"]

def play_game():

    chosen_word = random.choice(words)

    display = ["_"] * len(chosen_word)
    guessed_letters = []

    lives = 6
    game_over = False

    print("\nGuess the word one letter at a time!")
    print("You have", lives, "lives.\n")

    while not game_over:

        print("Word:", " ".join(display))
        print("Guessed letters:", " ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        # input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single valid letter.\n")
            continue

        # repeated guess check
        if guess in guessed_letters:
            print("⚠ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        # correct guess
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = guess
            print("✅ Correct!\n")

        # wrong guess
        else:
            lives -= 1
            print("❌ Wrong guess!")
            print("Lives left:", lives, "\n")

        # win condition
        if "_" not in display:
            print("🎉 You Win!")
            print("The word was:", chosen_word)
            game_over = True

        # lose condition
        if lives == 0:
            print("💀 You Lose!")
            print("The word was:", chosen_word)
            game_over = True


# replay system
while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != "y":
        print("\nThanks for playing! 👋")
        break