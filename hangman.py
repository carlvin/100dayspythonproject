import random

stages = ['''
    +---+
        |
        |
        |
        |
        |
 ============       
''','''
    +---+
    |   |
        |
        |
        |
        |
 ============       
''','''
    +---+
    |   |
    O   |
        |
        |
        |
 ============       
''','''
    +---+
    |   |
    O   |
    |\  |
        |
        |
 ============       
''','''
    +---+
    |   |
    O   |
   /|\  |
       |
        |
 ============       
''','''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 ============       
''','''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 ============       
''']

word_list = ['ardavark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(f'the chosen word is {chosen_word}')

display = []
loser_count = 10
word_length = len(chosen_word)


def judge(x):
    if x == 0:
        print("you loose")
    else:
        print('you win')


def empty_display(display, word_length):
    for _ in range(word_length):
        display += "_"

    print(display)


empty_display(display, word_length)

while "_" in display and loser_count != 0:
    guess = input('guess a letter \n').lower()

    for position, letter in enumerate(chosen_word):
        # letter = chosen_word[position]

        if letter == guess:
            # print(letter, position)
            display[position] = letter

    print(display)

judge(loser_count)
