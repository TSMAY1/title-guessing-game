import random

def get_titles(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents.strip().split('\n')
    
def pick_a_word(list_of_words):
    word = random.choice(list_of_words)
    return word.lower()

def main():
    print("Welcome to the Word Guesser Game!")
    print("=====================================\n\n")
    print("You will be given a random word to guess.")
    print("Try to guess the word in as few attempts as possible.\n")
    print("Please choose your category:")
    print("1. Board Game Titles")
    print("2. Book Titles")

    category = input("1 or 2?: ")

    if category not in ['1', '2']:
        print("Invalid choice. Please choose 1 or 2.")
        category = input("1 or 2?: ")
        
    if category == '1':
        path_to_file = "boardgame_titles.txt"
    
    if category == '2':
        path_to_file = "book_titles.txt"

    list_of_words = get_titles(path_to_file)
    word = pick_a_word(list_of_words)

    guessed_word = ['_'] * len(word)
    if " " in word:
        for i in range(len(word)):
            if word[i] == " ":
                guessed_word[i] = " "
    attempts = 10

    print("You have 10 attempts to guess the word.")
    print("Good luck!\n")

    while attempts > 0:
        print("Current word: " + ' '.join(guessed_word) + "\n")
        guess = input("Guess a letter: ")

        if len(guess) != 1:
            print("Please enter a single letter.\n")
            continue

        if guess.lower() in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Good guess!\n")

        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.\n")

        if '_' not in guessed_word:
            print("Congratulations! You've guessed the word: " + word)
            break
    
    if '_' in guessed_word:
        print("Sorry, you've run out of attempts. The word was: " + word)

if __name__ == "__main__":
    main()

