def start():
    print('********************')
    print('****HANGMAN GAME****')
    print('********************', end='\n\n')

    attempts = None
    bet_letters = []

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

        while attempts > 0:
            bet_letters.sort()
            print('--------------------------', end='\n\n')
            if len(bet_letters):
                print(', '.join(bet_letters))

            new_letter = input('Digit a new letter:').upper()

            if len(new_letter) != 1 or new_letter.isdigit():
                print('Wrong value informed. Put only one LETTER.')
            elif new_letter in bet_letters:
                print(f'Letter "{new_letter}" was been informed before. Try another one.')
            else:
                bet_letters.append(new_letter)

if(__name__ == "__main__"):
    start()
