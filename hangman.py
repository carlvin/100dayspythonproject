import random

stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 ============       
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 ============       
''', '''
    +---+
    |   |
    O   |
   /|\  |
       |
        |
 ============       
''', '''
    +---+
    |   |
    O   |
    |\  |
        |
        |
 ============       
''', '''
    +---+
    |   |
    O   |
        |
        |
        |
 ============       
''', '''
    +---+
    |   |
        |
        |
        |
        |
 ============       
''']

word_list = ['ardavark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(f'the chosen word is {chosen_word}')

display = []
wrong_guess = []
lives = 6
word_length = len(chosen_word)
# endgame = False

# display dashes for each letter in chosen word
for _ in range(word_length):
    display.append("_")

# 2
# prompt a user to guess a letter
# store letter in variable guess and convert to lowercase

# check for dashes and lives
while "_" in display and lives != 0:
    guess = input("Guess a letter \n").lower()
    # check if guess exists in a chosen word
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        wrong_guess.append(guess)
        print(stages[lives])
    print(display)
    print(f'Guessed Letters: {wrong_guess}')

if "_" not in display:
    print('you win!')
else:
    print("Game Over,You lost!")
    print(f'the correct word was: {chosen_word}')


