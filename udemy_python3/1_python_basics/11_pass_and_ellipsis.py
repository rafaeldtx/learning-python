# AULA 11 - pass e ellipsis

# pass e ellipsis são utilizados para pular blocos vazios sem emitir exceções

if True:
    ...
else:
    pass

# Exercícios propostos

# 1. Faça um programa que receba um número inteiro, informe se o número é par
# ou impar. Caso número não seja inteiro, informe um erro.
def program_1():
    try:
        num = int(input('Informe um número inteiro: '))

        if (num % 2) == 0:
            print(f'Número {num} é par!')
        else:
            print(f'Número {num} é ímpar!')
    except:
        print('Erro! Informe um número inteiro.')

# 2. Faça um programa que recebe a hora do usuário (digitada) e exiba
# saudação apropriada: bom dia 0-11, boa tarde 12-17 e boa noite 18-23
def program_2():
    hour = input('Informe uma hora (0-23): ')

    if not hour.isdigit():
        print('Erro! Informe uma hora entre 0 e 23.')
        return

    hour = int(hour)
    if hour < 0 or hour > 23:
        print('Erro! Informe uma hora entre 0 e 23.')
        return

    if hour <= 11:
        print('Bom dia!')
    elif hour <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')

# 3. Faça um programa que peça o primeiro nome do usuário. Caso o nome
# e retorne conforme regras:
# letras <= 4 "Nome curto"
# letras >= 5 e letras <= 6 "Nome normal"
# letras > 6 "Nome muito grande"
def program_3():
    name = input('Informe o seu nome: ')
    letters_count = len(name)

    if letters_count <= 4:
        print('Nome curto!')
    elif letters_count >= 5 and letters_count <= 6:
        print('Nome normal!')
    else:
        print('Nome grande!')

programs = { 1: program_1, 2: program_2, 3: program_3}

choice = input('Selecione um programa: ')
programs.get(int(choice))()
