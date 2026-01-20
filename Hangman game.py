import random

def play_hangman():
    # Predefined list of words
    words = ["python", "coding", "intern", "logic", "simple"]

    # Randomly select a word
    secret_word = random.choice(words)

    display_word = ["_"] * len(secret_word)
    guessed_letters = []
    remaining_attempts = 6

    print("\n🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")

    # Game loop
    while remaining_attempts > 0 and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Remaining attempts:", remaining_attempts)

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in secret_word:
            print("✅ Correct guess!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print("❌ Wrong guess!")
            remaining_attempts -= 1

    # Game result
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
    else:
        print("\n💀 Game Over! The word was:", secret_word)


# Play again option
while True:
    play_hangman()
    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("Thanks for playing! 👋")
        break
