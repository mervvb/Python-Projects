import random
from Hangman_words import word_list
from Hangman_arts import logo
from Hangman_arts import stages
print(logo)
lives = 6
end_of_game = False
chosen_word = random.choice(word_list)
#Testing code
#print(chosen_word)
word_length = len(chosen_word)
#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ")
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
       print(f"You've already guessed {guess}.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

     #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"This word waas {chosen_word}.")
    
    print(f"{''.join(display)}")

    #Check if user has got all letters.

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])











