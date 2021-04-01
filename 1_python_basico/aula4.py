# AULA 4 - Tipos de dados (primitivos)

# String - Textos, cadeia de caracteres cercados por aspas
# Int - Números (negativos ou positivos) inteiros
# Float - Números (negativos ou positivos) com ponto flutuante, números reais
# Boolean - True ou False (0 ou 1), valor lógico

# type() - Função para informar o tipo de classe da váriavel
print('string', type('string')) # ->  <class 'str'>
print(12345, type(12345)) # -> <class 'int'>
print(123.45, type(123.45)) # -> <class 'float'>
print(True, type(True), False, type(False)) # -> <class 'bool'> <class 'bool'>
print(10 == 10, type(10 == 10))

# CONVERSORES DE VÁRIVEIS

# str() - Função para converter o tipo de váriavel para string
print(str('10'), str('1.1244'), str(True), str(0.12), str(124))
# bool() - Função para converter o tipo de váriavel para booleano
print(bool('string'), bool(0.1244), bool(''))
# int() - Função para converter o tipo de váriavel para inteiro
print(int('10'), int(1.1244), int('0'))
# float() - Função para converter o tipo de váriavel para float
print(float('10'), float('1.1244'), float(True), float(0.12), float(124))

