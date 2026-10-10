# Dicionarios em Python
# Dicionarios são estruturados de dados que armazenam pares de "chave-valor". Eles são mutáveis, o que significa que você pode alterar seus valores após a criação.
# Chaves em dicionários devem ser únicas e imutáveis (como strings, números ou tuplas), enquanto os valores podem ser de qualquer tipo de dado.
# Usamos chaves {} para criar dicionários e os elementos são separados por vírgulas.
# Imutaveis: strings, números, tuplas, booleanos
# Mutaveis: listas, dicionarios, conjuntos

pessoa = {
    'nome': 'Antonio',
    'sobrenome': 'Santos',
    'idade': 21,
    'altura': 1.8,
    'enderecos': [
        {
            'rua': 'Rua A',
            'numero': 123,
            'cidade': 'São Paulo'
        }
    ]
}

print(pessoa['nome'])  # Acessando o valor associado à chave 'nome'

print(pessoa.keys())
print(pessoa.values())

# criando uma chave nova a partir de um dicionario existente
pessoa['peso'] = 75.5

# Criando uma chave dinamicamente a partir de uma variável
chave = 'telefone'
pessoa[chave] = '1234-5678'
print('Telefone adicionado')
print(pessoa)

del pessoa['telefone'] # Removendo a chave 'telefone' do dicionário
print('Telefone removido')
print(pessoa)

# Acessando um valor de uma chave que não existe no dicionário usando o método get()
if pessoa.get('telefone') is None:
    print('Telefone não encontrado')