# AULA 8 - Entrada de dados
# Requisição de valores ao usuário

# input() - Função de requisição de valor ao usuário. Sempre recebe string

name = input('Qual o seu nome? ')
print(f'Seja bem-vindo {name}')

age = input('Qual a sua idade? ')
born_at = 2021 - int(age)
print(f'Legal! Você nasceu em {born_at}!')
