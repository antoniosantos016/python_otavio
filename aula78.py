# Sets - Conjuntos em Python
# Conjuntos são coleções de elementos únicos, ou seja, não permitem elementos duplicados. Em Python, os conjuntos são representados pelo tipo `set`.
# Conjuntos são úteis para operações matemáticas como união, interseção e diferença.
# Sets em Python são mutáveis, o que significa que você pode adicionar ou remover elementos após a criação do conjunto.
# Porém, os elementos dentro de um conjunto devem ser de tipos imutáveis, como números, strings ou tuplas.

# s1 = set('Antonio')
s1 = {'Antonio', 1, 2, 3}
print(s1)  

# Sets são eficientes para remover duplicatas de uma lista. Por exemplo, se você tiver uma lista com elementos repetidos, você pode convertê-la em um conjunto para obter apenas os elementos únicos.
# Seus valores são únicos, então se você tentar adicionar um valor que já existe no conjunto, ele não será adicionado novamente.
s1.add(3)  # Adicionando um elemento ao conjunto
print(s1)

s2 = {3, 3, 3, 1}
print(s2)  # Mostrando que elementos duplicados não são adicionados

lista = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
s3 = set(lista)
print(s3)  # Mostrando que duplicatas foram removidas