import random

def start():
    secret_word = random.choice(get_secret_words_list()).upper()
    right_letters = ["_" for letter in secret_word]
    attempts = set_difficulty_attempts(len(secret_word))
    bet_letters = []

    print('********************')
    print('****HANGMAN GAME****')
    print('********************', end='\n\n')

    while attempts > 0:
        show_bet_letters = ', '.join(bet_letters)

        print('--------------------------', end='\n\n')
        print(f"You have {attempts} attempt(s) remaining.", end='\n\n')
        print(f"BETS: {show_bet_letters}")
        print(f"WORD: {' '.join(right_letters)}", end='\n\n')

        new_bet_letter = input('Digit a new letter:').strip().upper()

        if right_bet(new_bet_letter, bet_letters):
            if new_bet_letter not in secret_word:
                attempts -= 1

            bet_letters.append(new_bet_letter)
            bet_letters.sort()

            right_letters = set_right_letters(secret_word, new_bet_letter, right_letters)
        else:
            if new_bet_letter in bet_letters:
                print(f'Letter "{new_bet_letter}" was been informed before. Try another one.')
            else:
                print('Wrong value informed. Put only one LETTER.')

        if '_' not in right_letters:
            print(f'Congratulations! You right the secret word: "{secret_word}"!')
            break
        elif attempts == 0:
            print(f'You Lose! The secrect word was {secret_word}')

def set_difficulty_attempts(word_length):
    attempts = None

    while attempts == None:
        print('Inform the difficulty level')
        print('1- Easy \n2- Medium \n3- Hard')
        level = int(input('Put the difficulty: '))

        if level == 1:
            attempts = round(2.5 * word_length)
        elif level == 2:
            attempts = round(2.0 * word_length)
        elif level == 3:
            attempts = round(1.5 * word_length)
        else:
            print('Not valid level. Insert between 1 and 3', end='\n\n')

    return attempts

def set_right_letters(secret_word, new_bet_letter, right_letters):
    for index in range(0, len(secret_word)):
        secret_letter = secret_word[index].upper()

        if new_bet_letter == secret_letter:
            right_letters[index] = secret_letter

    return right_letters

def get_secret_words_list():
    secret_words_file = open("secret_words.txt", "r")
    return [word_line.strip() for word_line in secret_words_file]

def right_bet(new_bet, bet_list):
    return(
        len(new_bet) == 1 and
        not new_bet.isdigit() and
        new_bet not in bet_list
    )

if(__name__ == "__main__"):
    start()
