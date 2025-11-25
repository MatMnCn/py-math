class Trabalhador:

# Primeiro Membro da Classe - Atributos
    __nome:str
    __jornada:float

# Segundo Membro da Classe - Propriedade
# Propriedade do atributo nome 
    @property
    def _nome(self) -> str:
        return self.__nome
    @_nome.setter
    def _nome(self, nome:str) -> str:
        if nome == "" or nome == None:
            raise ValueError('Nome inválido')
        else:
            self.__nome = nome

# Propriedade do atributo jornada 
    @property
    def _jornada(self) -> float:
        return self.__jornada
    @_jornada.setter
    def _jornada(self, jornada:float) -> float:
        if jornada <= 0 or jornada == None:
            raise ValueError('Jornada inválida')
        else:
            self.__jornada = jornada

# Terceiro membro da Classe - Construtor
    def __init__(self, nome:str, jornada:float):
        self._nome = nome
        self._jornada = jornada
        
# Quarto Membro da Classe - Métodos 
    def pagamento(self) -> float:
        pass
# Fim de Super Classe Trabalhador

class EmpregadoSenai(Trabalhador):

# Primeiro Membro da Classe - Atributos 
    _ValorPorHora:float

# Segundo Membro da Classe - Propriedade
    @property
    def _ValorPorHora(self) -> float:
        return self.__ValorPorHora
    @_ValorPorHora.setter
    def _ValorPorHora(self, valor) -> float:
        if valor <= 0 or valor == None:
            raise ValueError('Valor por hora inválido')
        else:
            self.__ValorPorHora = valor

# Terceiro Membro da Classe - Construtor
    def __init__(self, nome, jornada, valor):
        super().__init__(nome, jornada)
        self._ValorPorHora = valor

# Quarto Membro da Classe - Métodos
    def pagamento(self) -> float:
        pagamento = self._jornada * self._ValorPorHora
        return pagamento
# Fim de Sub Classe EmpregadoSenai

class Terceirizado(EmpregadoSenai):

# Primeiro Membro da Classe - Atributos
    __adicional = 0.2

# Segundo Membro da Classe - Construtor
    def __init__(self, nome, jornada, valor):
        super().__init__(nome, jornada, valor)

# Terceiro Membro da Classe - Métodos
    def pagamento(self) -> float:
        pagamento = super().pagamento() * (1 + self.__adicional)
        return pagamento
# Fim de Sub Sub Classe Terceirizado
# Inicio Codigo Principal
lista = []
funcionario:Trabalhador

def main():
    quantidade = int(input("Digite a quantidade de funcionarios a ser inserida: "))

    for i in range(quantidade):
        print(f"Colaborador n° {i+1}")
        colaborador = input("O colaborador eh terceirazado (s/n) ? ")
        nome = input("Nome do colaborador: ")
        horas = int(input("Horas trabalhadas: "))
        valor = float(input("Valor da hora do colaborador: "))
        if colaborador is "s":
            funcionario  = Terceirizado(nome, horas, valor)
        else:
            funcionario = EmpregadoSenai(nome, horas, valor)
        lista.append(funcionario)
    print("\nPagamentos dos Colaboradores")
    for i in range(quantidade):
        print(f"{colaborador._nome} - R$ {colaborador.pagamento():.2f}")

if __name__ == "__main__":
    main()
# Fim Codigo Principal