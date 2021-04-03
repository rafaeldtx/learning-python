# AULA 10 - Funções built-in

num1 = input('Informe um número: ')
num2 = input('Informe outro número: ')

print(num1, 'isnumeric()', num1.isnumeric())
print(num2, 'isnumeric()', num2.isnumeric(), end='\n\n')

print(num1, 'isdigit()', num1.isdigit())
print(num2, 'isdigit()', num2.isdigit(), end='\n\n')

print(num1, 'isdecimal()', num1.isdecimal())
print(num2, 'isdecimal()', num2.isdecimal(), end='\n\n')

# uso de try/except
try:
    print(f'{num1} + {num2} = ', float(num1) + float(num2))
except:
    print('Erro! Favor informar apenas números.')

