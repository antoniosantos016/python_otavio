# Métodos uteis dos dicionários em Python
# len - retorna a quantidade de chaves do dicionário
# keys - retorna as chaves do dicionário
# values - retorna os valores do dicionário
# items - retorna os itens do dicionário
# setdefault - retorna o valor da chave informada, caso não exista, insere a chave com o valor informado
# copy - retorna uma cópia rasa (shallow copy) do dicionário

pessoa = {
  'nome': 'Antonio',
  'sobrenome': 'Santos',
#   'idade': 30,
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])

# print(len(pessoa))

# # print(tuple(pessoa.keys()))
# # print(list(pessoa.values()))
# print(list(pessoa.items()))

# for chave in pessoa.keys():
#     print(chave)

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)