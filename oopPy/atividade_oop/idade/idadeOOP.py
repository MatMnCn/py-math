class Pessoa:
    nome: str
    idade: int

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def maior_idade(self, segunda):
        if self.idade > segunda.idade:
            return self
        elif segunda.idade > self.idade:
            return segunda
        else:
            return None  # 

    def saida(self, segunda):
        pessoa_mais_velha = self.maior_idade(segunda)

        if pessoa_mais_velha is None:
            return "As idades das duas pessoas são iguais."
        else:
            return f"Pessoa com a maior idade: {pessoa_mais_velha.nome} com {pessoa_mais_velha.idade} anos."
