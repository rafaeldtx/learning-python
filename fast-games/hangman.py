def start():
    print('********************')
    print('****HANGMAN GAME****')
    print('********************', end='\n\n')

    bet_letters = []
    secret_word = 'banana'
    right_letters = []

    for letter in secret_word:
        right_letters.append('_')

    attempts = calls_difficulty_attempts()

    while attempts > 0:
        bet_letters.sort()

        print('--------------------------', end='\n\n')
        if len(bet_letters):
            print(f"CHUTES: {', '.join(bet_letters)}", end='\n\n')

        print(f"PALAVRA: {' '.join(right_letters)}", end='\n\n')

        new_letter = input('Digit a new letter:').upper()

        if len(new_letter) != 1 or new_letter.isdigit():
            print('Wrong value informed. Put only one LETTER.')
        elif new_letter in bet_letters:
            print(f'Letter "{new_letter}" was been informed before. Try another one.')
        else:
            bet_letters.append(new_letter)

            for index in range(0, len(secret_word)):
                secret_letter = secret_word[index].upper()

                if new_letter == secret_letter:
                    right_letters[index] = secret_letter


def calls_difficulty_attempts():
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

if(__name__ == "__main__"):
    start()
