import random
from art import stages, logo
from words import word_list

# display the logo and set the game to not done
# set the lives to the number of stages of the hangman art
print(logo)
done = False
lives = len(stages) - 1

# a random word from the words list is picked
chosen_word = random.choice(word_list)
# define the length of the word
word_length = len(chosen_word)

# set display as an empty list
display = []
# add _ with the same number of chars in the chosen word
for _ in range(word_length):
    display += "_"

# start the game with asking the first letter and loop it until the done is set to true
while not done:
    guess = input("Guess a letter: ").lower()

    # if the letter is already guessed, display the message
    if guess in display:
        print(f"You've already guessed {guess}")

    # if the user guessed the correct letter, replace the _ in the display with the correct letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # display the list of letters and _ from the display list and joined them together
    print(f"{' '.join(display)}")

    # if the user guessed the wrong letter, they lose a life
    if guess not in chosen_word:
        print(f"You guessed {guess}, that letter is not in the word. You lose a life")
        lives -= 1
        # if the user used all of their life, they lose the game
        if lives == 0:
            done = True
            print(f"You lose. The word is {chosen_word}")

    # if the user guessed all the letters correctly, the game finished and the user wins
    if not "_" in display:
        done = True
        print("You win!")

    # print the currect stages of the word
    print(stages[lives])