import guess
import hangman

print('*****************')
print('****HUB GAMES****')
print('*****************', end='\n\n')


print('Which game do you want to play?')
print('1- Guess \n2- Hangman', end='\n\n')

game_choice = int(input('Put the game number:'))
print('------------------------------', end='\n\n')

if game_choice == 1:
    guess.start()
elif game_choice == 2:
    hangman.start()
else:
    print('Invalid value. Put one in the list.')

