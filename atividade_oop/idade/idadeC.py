import idadeOOP as p

# Entrada de dados
print("Entre com os dados das pessoas:")

nome1 = input("Nome da 1º Pessoa: ")
idade1 = int(input("Idade da 1º Pessoa: "))

nome2 = input("Nome da 2º Pessoa: ")
idade2 = int(input("Idade da 2º Pessoa: "))

# Criando objetos
p1 = p.Pessoa(nome1, idade1)
p2 = p.Pessoa(nome2, idade2)

# Impressão manual
print(f'''
Dados das pessoas:
    Nome da 1º pessoa: {p1.nome}
    Nome da 2º pessoa: {p2.nome}
    Idade da 1º pessoa: {p1.idade} anos
    Idade da 2º pessoa: {p2.idade} anos
    Pessoa com a maior idade: {p2.p_maior_idade(idade1, nome1)} com {p2.maior_idade(idade1)} anos.
''')
