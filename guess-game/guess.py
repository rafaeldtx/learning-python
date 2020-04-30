print('***********************')
print('*******Guess Game******')
print('***********************')

secret_number = 43
attempts = 5

while(attempts > 0):
  print(f'{attempts} tentativas restantes', end="\n\n")
  bet_number = int(input('Write your number:'))
  attempts -= 1

  print(f'Your number is: {bet_number}', sep=' ', end="\n\n")

  if(bet_number == secret_number):
    print("Congratulations! You're right!!!")
    break
  else:
    print("You're wrong. Try again", end="\n\n")
    if(bet_number > secret_number):
      print(f"TIP: The secret number is below of {bet_number}", end="\n\n")
    else:
      print(f"TIP: The secret number is above of {bet_number}", end="\n\n")
  print('------------------------------------------', end='\n\n')



print('End game')
