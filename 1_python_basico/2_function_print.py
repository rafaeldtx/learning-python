# AULA 2 - O comando print()

# ==USO DE FUNÇÃO print()
print(12345)
print('Rafael', 'Domingues', 'Teixeira', 12345) # CONCATENAÇÃO DE PARAMS

'''
== ARGUMENTOS NOMEADOS
sep: utilizado para adicionar valor para concatenação de args
end: utilzado para mudar comportamento final do print.
Por padrão atribui quebra de linha "\n"
'''
print('João', 'Maria', sep=' - ', end='.\n')
print('FIM')

# OBS: Python diferencia letras maiusculas e minusculas para chamada de funções
# Ex: print() != Print()

# DESAFIO
# Exibir cpf formatado
print('123','456','789', sep='.', end='.10')
