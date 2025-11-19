class Pessoa:

    nome:str
    idade:int
    
    # Construtor
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        

    # Metodos
    def maior_idade(self, idade):
        if self.idade > idade:
            return self.idade
        elif self.idade < idade:
            return idade
        else:
            return "As idades das duas pessoas são iguais ;)"

    def p_maior_idade(self, idade, nome):
        if self.idade > idade:
            return self.nome
        elif self.idade < idade:
            return nome
        else:
            return ""

    def saida(self,idade,nome):
        return f'''
Dados das pessoas:
\tNome da 1º pessoa: {nome}
\tNome da 2º pessoa: {self.nome}
\tIdade da 1º pessoa: {idade} anos.
\tIdade da 2º pessoa: {self.idade} anos.
\tPessoa com a maior idade: {self.p_maior_idade()} com {self.maior_idade()} anos.
'''
