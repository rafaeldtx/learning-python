# AULA 9 - CONDICIONAIS

# if:,  elif:, else:

# BOOLEANS
if False:
    print('Isso é falso. :X')
elif True:
    print('Isso é verdadeiro!')

if False:
    print('Isso não será exibido. :(')
else:
    print('Isso sim é exibido! o/')

# OPERADORES RELACIONAIS
# == > >= < <= !=
if True != False and 1 == 1:
    print('Isso é verdadeiro!')
if 2 > 1 and 2 >= 3:
    print('Isso nunca será exibido!')
else:
    print('Falso! 2 é maior que 1, mas não é maior ou igual a 3!')

# OPERADORES LÓGICOS
# and, or, not, in, not in
if not 1 < 0: # inversor de lógica "!resultado"
    print('Isso é Verdadeiro')
if 'a' in 'Rafael': # Verifica se há valor em determinada variavel
    print('Rafael possui a letra A')
if 'w' not in 'Rafael': # Verifica se não há valor em determinada variavel
    print('Rafael não possui a letra W')
