import random

word_list = ['ardavark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(f'the chosen word is {chosen_word}')

display = []

for _ in range(len(chosen_word)):
    display += "_"

print(display)

loser_count = 10

while "_" in display and loser_count != 0:
    guess = input('guess a letter \n').lower()

    for position, letter in enumerate(chosen_word):
        # letter = chosen_word[position]

        if letter == guess:
            #print(letter, position)
            display[position] = letter
        else:
            loser_count -= loser_count
    print(display)

if loser_count == 0:
    print("you loose")
else:
    print('you win')
