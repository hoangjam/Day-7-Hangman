import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed the right letter {guess}")
    
    if guess in guessed_letters:
        print(f"NOTE: {guess} has already been guessed")
        print(f"Guessed letters: {guessed_letters}")
    else:
        guessed_letters.append(guess)
        print(f"Guessed letters: {guessed_letters}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You've guessed {guess}, add a body part.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])