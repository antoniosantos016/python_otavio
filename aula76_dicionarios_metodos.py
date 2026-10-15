p1 = {
    'nome': 'Antonio',
    'sobrenome': 'Santos',
}

# pop - apaga o item do dicionário e retorna o valor

nome = p1.pop('nome')
print(nome)  
print(p1)  

# popitem - apaga o último item do dicionário e retorna uma tupla com a chave e o valor
ultimo_item = p1.popitem()
print(ultimo_item)
print(p1)

# update - atualiza o dicionário com os itens de outro dicionário
p1.update({
    'nome': 'Antonio',
    'idade': 30,
})
print(p1)

p1.update(nome='João', sobrenome='Silva')
print(p1)

tupla = ('nome', 'nova_tupla'),
p1.update(tupla)
print(p1)

lista = ['nome', 'nova_lista'],
p1.update(lista)
print(p1)