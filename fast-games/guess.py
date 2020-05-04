import random

def start():
    print('***********************')
    print('*******Guess Game******')
    print('***********************', end='\n\n')

    secret_number = random.randrange(1,101)
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

        while(attempts > 0):
            print('------------------------------------------', end='\n\n')

            print(f'{attempts} tentativas restantes', end="\n\n")
            bet_number = int(input('Write your number between 1 and 100: '))
            attempts -= 1

            if bet_number < 1 or bet_number > 100:
                print('Wrong bet! Put a bet between 1 and 100!', end='\n\n')
                continue
            else:
                print(f'Your number is: {bet_number}', sep=' ', end="\n\n")

            if(bet_number == secret_number):
                print("Congratulations! You're right!!!")
                break
            else:
                print("You're wrong.")
            if(bet_number > secret_number):
                print(f"TIP: The secret number is below of {bet_number}", end="\n\n")
            elif(attempts != 0):
                print(f"TIP: The secret number is above of {bet_number}", end="\n\n")
            else:
                print(f"You lose! The secret number is {secret_number}")



    print('End game')
