import random

def start():
    secret_word = random.choice(secret_words_list())
    right_letters = ["_" for letter in secret_word]
    attempts = get_difficulty_attempts()
    bet_letters = []

    print('********************')
    print('****HANGMAN GAME****')
    print('********************', end='\n\n')

    while attempts > 0:
        show_bet_letters = ', '.join(bet_letters)

        print('--------------------------', end='\n\n')
        print(f"CHUTES: {show_bet_letters}")
        print(f"PALAVRA: {' '.join(right_letters)}", end='\n\n')

        new_bet_letter = input('Digit a new letter:').strip().upper()

        if len(new_bet_letter) != 1 or new_bet_letter.isdigit():
            print('Wrong value informed. Put only one LETTER.')
        elif new_bet_letter in bet_letters:
            print(f'Letter "{new_bet_letter}" was been informed before. Try another one.')
        else:
            bet_letters.append(new_bet_letter)
            bet_letters.sort()

            get_right_letters(secret_word, new_bet_letter, right_letters)

def get_difficulty_attempts():
    attempts = None

    while attempts == None:
        print('Inform the difficulty level')
        print('1- Easy \n2- Medium \n3- Hard')
        level = int(input('Put the difficulty: '))

        if level == 1:
            attempts = 12
        elif level == 2:
            attempts = 8
        elif level == 3:
            attempts = 4
        else:
            print('Not valid level. Insert between 1 and 3', end='\n\n')

    return attempts

def get_right_letters(secret_word, new_bet_letter, right_letters):
    for index in range(0, len(secret_word)):
        secret_letter = secret_word[index].upper()

        if new_bet_letter == secret_letter:
            right_letters[index] = secret_letter

    return right_letters

def secret_words_list():
    return [
        'apple',
        'avocado',
        'banana',
        'cucumber',
        'grape',
        'lettuce',
        'pineapple',
        'pumpkin',
        'tomato',
    ]

if(__name__ == "__main__"):
    start()
