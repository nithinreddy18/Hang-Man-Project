import os

def show_hangman(tries):
    stages = [
        # Final state: head, body, arms, and legs
        """
           ||=====
           ||    |
           ||   \\O/
           ||    |
           ||   / \\
           ||      
        """,
        # Head, body, arms, and one leg
        """
           ||=====
           ||    |
           ||   \\O/
           ||    |
           ||    /
           ||      
        """,
        # Head, body, and arms
        """
           ||=====
           ||    |
           ||   \\O/
           ||    |
           ||      
           ||      
        """,
        # Head and one arm
        """
           ||=====
           ||    |
           ||   \\O/
           ||      
           ||      
           ||      
        """,
        # Head only
        """
           ||=====
           ||    |
           ||   \\O
           ||      
           ||      
           ||      
        """,
        # Only gallows
        """
           ||=====
           ||    |
           ||    O
           ||      
           ||      
           ||      
        """,
        # Initial empty gallows
        """
           ||=====
           ||    |
           ||      
           ||      
           ||      
           ||      
        """
    ]
    return stages[tries]


def hangman():
    print("\n\nWelcome to the HANGMAN GAME!\n")
    print("You will get 6 chances to guess the correct word.")
    print("Help the man survive... Good luck!\n")

    # Get the secret word
    word = input("Enter the secret word (lowercase letters only): ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen so opponent can't see

    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    tries = 6

    while tries > 0 and "_" in guessed_word:
        print(show_hangman(tries))
        print("Word: ", " ".join(guessed_word))
        print(f"Tries left: {tries}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")

        guess = input("\nEnter a letter (a-z): ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single lowercase letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            tries -= 1

    # End of game
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print(show_hangman(tries))
        print("\n💀 Game Over! The word was:", word)


if __name__ == "__main__":
    hangman()
