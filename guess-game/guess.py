print('***********************')
print('*******Guess Game******')
print('***********************')

secret_number = 43

bet_number = input('Write your number:')

print('Your number is:', bet_number, sep=' ')

if(int(bet_number) == secret_number):
  print("You're right!!!")
else:
  print("You're wrong. Try again")
