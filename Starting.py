import random
from hangman import stages, logo
from wordlist import word_list

print(logo)

chosen_word = random.choice(word_list)
letter_list = list(chosen_word)
word_lenght = len(chosen_word)
display = []
for _ in range(word_lenght):
    display += '_'

end_of_game = False
lives = 6
while not end_of_game:
    print(' '.join(display))
    guess = input('Guess a letter: \n').lower()
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f'You guessed {guess}, it is not in the word. You lost a life.')
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('You lose.')
            print(f'The word was: {chosen_word}')
    if '_' not in display:
        end_of_game = True
        print('You win.')
    print(stages[lives])

while True:
    pass
