# ABC (A*bstract *Base Classes)

# Com duck typing, você ganha muita flexibilidade ao não precisar ficar preso
# aos tipos dos objetos, só que em alguns momentos você pode querer ter
# restrições, como de uma garantia que uma classe implemente os métodos que
# você quer.

# Em outras linguagens, há a ideia de classes e métodos abstratos, que forçam
# as classes filhas a implementar alguns métodos.

# Para fazer o mesmo no Python, é possível usar classes abstratas, as chamadas
# ABC (A*bstract *Base Classes). Existem classes já prontas que ajudam nessa
# ideia.

from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    pass

objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)

# O código acima apresenta um erro, dizendo que você esqueceu de implementar
# todos os métodos necessários para tornar a classe uma MutableSequence.

# Sempre que você quiser garantir a implementação de alguns métodos, pode
# recorrer às classes já existentes em collections.abc e outros pacotes também.
