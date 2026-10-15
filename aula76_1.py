# Manipulando chaves e valores em dicionários
pessoa = {

}

chave = 'nome'
pessoa[chave] = 'Antonio'


print(pessoa[chave])
pessoa['sobrenome'] = 'Silva'

pessoa[chave] = 'Maria'
print(pessoa)

del pessoa['sobrenome']
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome', None) is None:
    print('Não existe sobrenome')
else:
    print(pessoa['sobrenome'])