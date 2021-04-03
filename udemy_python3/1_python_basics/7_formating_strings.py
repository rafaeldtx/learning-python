# AULA 7 - Formatação de strings

# uso de 'f' antes da iniciação de string permite atribuir variaves
# em '{}' dentro de strings

name = 'Rafael'
surname = 'Domingues'
age = 24

print(f'Meu nome é {name} {surname}')
print('Meu nome é {} {}'.format(name, surname))
print('Meu nome é {1} {0}'.format(name, surname))
print('Meu nome é {n} {s}'.format(n=name, s=surname))
print('Tenho {:.2f} anos'.format(age))
