# AULA 12 - Formatando valores com modificadores

# :s - Texto (strings)
# :d - Inteiros (int)
# :f - Números de ponto flutuante (float)
# :.(Número)f - Quantidade de casas decimais (float)
# :(caracter)(> || < || ^)(quantity)(tipo - s, d ou f)

# > - caracteres à esquerda
# < - caracteres à direita
# ^ - caracteres divididos ao lado

name = 'joao'
int_num = 10
float_num = 10.00

# :s
print(f'{name:s}') # -> "joao"

# :f
print(f'{float_num:f}') # -> 10.000000
print(f'{int_num:f}') # -> 10.000000

# :d
print(f'{int_num:d}') # -> 10

# :.<num>f
print(f'{int_num:.3f}') # -> 10.000

# :(char)<(quantity)s
print(f'{name:#<10}') # -> joao######
print(name.ljust(10, '#')) # -> joao######
# :(char)>(quantity)s
print(f'{name:#>10}') # -> ######joao
print(name.rjust(10, '#')) # -> joao######
# :(char)^(quantity)s
print(f'{name:#^10}') # -> ###joao###
print(name.center(10, '#')) # -> joao######
