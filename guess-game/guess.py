print('***********************')
print('*******Guess Game******')
print('***********************')

secret_number = 43

bet_number = int(input('Write your number:'))

print('Your number is:', bet_number, sep=' ')

if(bet_number == secret_number):
  print("You're right!!!")
else:
  print("You're wrong. Try again")
  if(bet_number > secret_number):
    print("TIP: The secret number is below of", bet_number)
  else:
    print("TIP: The secret number is above of", bet_number)

