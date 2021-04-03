# AULA 14 - WHILE LOOPS

# While - Repetição de bloco enquanto valor persistir
x = 1
while x <= 10:
    if x == 3: # pular bloco quando for 3
        x += 1
        continue

    print(x, end=' ')
    x += 1

# tabuada do 1 ao 10
x = 1
while x <= 10:
    print('{:#^20}'.format(f' tabuada do {x} '))

    y = 1
    while y <= 10:
        print(f'{x} x {y} = ', (x*y))
        y += 1

    x += 1
    print()
else: # FUNCIONA APENAS CASO WHILE SEJA EXECUTADO SEM USO DO break
    print('Fim do loop while', end='\n\n')

# ITERANDO STRINGS COM WHILE
string = 'o rato roeu a roupa do rei de roma' # Iterável
count = 0
new_string = ''

while count < len(string):
    new_string += string[count]
    count += 1

print(new_string)
