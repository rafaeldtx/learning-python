print('***********************')
print('*******Guess Game******')
print('***********************')

secret_number = 43
attempts = 5

while(attempts > 0):
  bet_number = int(input('Write your number:'))

  print(attempts,'tentativas restantes', end="\n\n")
  attempts -= 1

  print('Your number is:', bet_number, sep=' ', end="\n\n")

  if(bet_number == secret_number):
    print("You're right!!!")
    break
  else:
    print("You're wrong. Try again", end="\n\n")
    if(bet_number > secret_number):
      print("TIP: The secret number is below of {}".format(bet_number), end="\n\n")
    else:
      print("TIP: The secret number is above of {}".format(bet_number), end="\n\n")

print('End game')
