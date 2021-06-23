word = input("Please enter a word to start the game: ")

word_listed_no_dups = set(word)

guess_list = []

letter_success_counter = 0

guesses = 0


def check_guess(guess_inputted):
    if guess_inputted in word_listed_no_dups and guess not in guess_list:
        return True
    else:
        return False


while guesses != 5:
    guess = input("Type a letter: ")
    check = check_guess(guess)
    if check:
        print("You got a letter!")
        guess_list.append(guess)
        print("Letters guessed so far: " + str(guess_list))
        letter_success_counter += 1
        if letter_success_counter == len(word_listed_no_dups):
            print("You got it! The word was: " + word)
            break
    else:
        guesses += 1
        if guesses == 5:
            print("You failed! The word was: " + word)
            break
        print("Try again! You have " + str(5 - guesses) + " guesses remaining.")
