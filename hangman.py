import random

stages = ['''
    +---+
        |
        |
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
    O   |
    |\  |
        |
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
   /|\  |
   /    |
        |
 ============       
''', '''
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
endgame = False


def judge():
    if "_" not in display:
        print('you win')
    else:
        endgame = True
        print("you loose")


def empty_display(display, word_length):
    for _ in range(word_length):
        display += "_"

    print(display)


empty_display(display, word_length)

while not endgame:
    guess = input('guess a letter \n').lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            # print(letter, position)
            display[position] = letter

    print(display)

judge(loser_count)
