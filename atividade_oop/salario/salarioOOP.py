class Funcionario:
    #Classe para armazenar nome e salário

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

class CalculadoraSalario:
    #Classe da formula

    def media(self, f1, f2):
        return (f1.salario + f2.salario) / 2
