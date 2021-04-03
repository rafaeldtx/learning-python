# AULA 13 - Manipulando strings

# Strings indices - string[0] || string[-1]...
# Fatiamento de string - [inicio:fim:passo]
# Funções built-in len, abs, type, print, etc...
# Essas funções podem ser usadas diretamente em cada tipo

# positives  [012345678]
string     = '123456789'
# negatives -[987654321]

# Retorna valor do indice
print(string[0]) # -> '1'
print(string[-1]) # -> '9'

# Fatiar string do começo até o indice
print(string[:8]) # -> '12345678'
print(string[:-1]) # -> '12345678'

# Fatiar string do indice até o final
print(string[1:]) # -> '23456789'
print(string[-8:]) # -> '23456789'

# Fatiar string parcial
print(string[3:6]) # -> '456'
print(string[-6:-3]) # -> '456'

# Fatiar string com passo (pulo de indices)
print(string[::2]) # -> '13579'
print(string[::3]) # -> '147'
print(string[3:6:2]) # -> '46'
print(string[:6:2]) # -> '135'
print(string[3::2]) # -> '468'

