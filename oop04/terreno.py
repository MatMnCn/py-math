class Terreno:

    # Construtores
    def __init__(self, largura: float, comprimento: float):
        self.largura = largura
        self.comprimento = comprimento

    # Propriedades
    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, largura: float):
        self.__largura = largura

    @property
    def comprimento(self):
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, comprimento: float):
        self.__comprimento = comprimento

    # Métodos privados
    def __area(self) -> float:
        return self.comprimento * self.largura

    def __preco(self, preco: float) -> float:
        return self.__area() * preco   # ← corrigido

    # Método público
    def dadosTerreno(self, preco: float) -> str:
        saida = f'''
Largura: {self.largura}
Comprimento: {self.comprimento}
Área: {self.__area():.2f}
Preço: {self.__preco(preco):.2f}
'''
        return saida


# Entrada de dados
try:
    largura = float(input("Digite a largura do terreno: "))
    comprimento = float(input("Digite o comprimento do terreno: "))
    preco = float(input("Digite o preço do metro quadrado: "))

    # Instanciar
    terreno = Terreno(largura, comprimento)

    # Saída de dados
    print(terreno.dadosTerreno(preco))

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número válido.")
except Exception as e:
    print(f"Erro: {e}")