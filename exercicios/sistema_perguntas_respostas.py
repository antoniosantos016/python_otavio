perguntas = [
    {
        'Pergunta': 'Qual é a capital da França?',
        'Opcoes': ['1) Paris', '2) Londres', '3) Berlim', '4) Madrid'],
        'Resposta': '1'
    },
    {
        'Pergunta': 'Qual é a capital da Alemanha?',
        'Opcoes': ['1) Paris', '2) Londres', '3) Berlim', '4) Madrid'],
        'Resposta': '3'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['1) 2', '2) 5', '3) 10', '4) 20'],
        'Resposta': '2'
    }
]

print("Bem-vindo ao Sistema de Perguntas e Respostas!")
print("Responda às perguntas digitando o número correspondente à opção correta.")

pontuacao = 0

for pergunta in perguntas:
    print("\n" + pergunta['Pergunta'])
    for opcao in pergunta['Opcoes']:
        print(opcao)
    
    resposta_usuario = input("Digite o número da sua resposta: ")
    
    if resposta_usuario == pergunta['Resposta']:
        print("Resposta correta!")
        pontuacao += 1
    else:
        print("Resposta incorreta. A resposta correta é:", pergunta['Resposta'])

print("\nVocê acertou", pontuacao, "de", len(perguntas), "perguntas.")