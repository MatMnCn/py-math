from abc import ABC, abstractmethod

# Super classe Contribuinte
class Contribuinte(ABC):
    # 1° Membro - Atributos
    __nome: str
    __renda_anual: float

    # 2° Membro - Propriedades
    @property
    def _nome(self) -> str:
        return self.__nome
    @_nome.setter
    def _nome(self, nome: str) -> None:
        if not nome or len(nome.strip()) < 2:
            raise ValueError("Nome inválido")
        self.__nome = nome

    @property
    def _renda_anual(self) -> float:
        return self.__renda_anual
    @_renda_anual.setter
    def _renda_anual(self, renda: float) -> None:
        if renda < 0:
            raise ValueError("Renda negativa não permitida")
        self.__renda_anual = renda

    # 3° Membro - Construtor
    def __init__(self, nome: str, renda_anual: float):
        self._nome = nome 
        self._renda_anual = renda_anual 

    # 4° Membro - Método 
    @abstractmethod
    def calcular_imposto(self) -> float:
        pass

    def exibir_dados(self) -> str:
        imposto = self.calcular_imposto() 
        return f"Nome: {self._nome}, Renda: R$ {self._renda_anual:,.2f}, Imposto: R$ {imposto:,.2f}"
# Fim de Super Classe Contribuinte

#Subclasse - PessoaFisica
class PessoaFisica(Contribuinte):

    # 1° Membro - Atributo
    __gastos_saude: float
    
    # 2° Membro - Propriedade
    @property
    def _gastos_saude(self) -> float:
        return self.__gastos_saude
    @_gastos_saude.setter
    def _gastos_saude(self, gastos: float) -> None:
        if gastos < 0:
            raise ValueError("Gastos de saude nao podem ser negativos")
        self.__gastos_saude = gastos
        
    # 3° Membro - Construtor
    def __init__(self, nome: str, renda_anual: float, gastos_saude: float):
        super().__init__(nome, renda_anual)
        self._gastos_saude = gastos_saude
        
    # 4° Membro 
    def calcular_imposto(self) -> float:
        renda = self._renda_anual

        aliquota = 0.15 if renda < 20000.00 else 0.25
        
        imposto_bruto = renda * aliquota
        
        # Baixa de 1/2
        baixa = self._gastos_saude * 0.50
        
        imposto_liquido = imposto_bruto - baixa
        
        return max(0, imposto_liquido)

#Subclasse - PessoaJuridica
class PessoaJuridica(Contribuinte):
    
    # 1° Membro - Atributo
    __numero_funcionarios: int
    
    # 2° Membro - Propriedade
    @property
    def _numero_funcionarios(self) -> int:
        return self.__numero_funcionarios
    @_numero_funcionarios.setter
    def _numero_funcionarios(self, num: int) -> None:
        if num < 0:
            raise ValueError("Número de funcionarios invalido")
        self.__numero_funcionarios = num
        
    # 3° Membro - Construtor
    def __init__(self, nome: str, renda_anual: float, numero_funcionarios: int):
        super().__init__(nome, renda_anual)
        self._numero_funcionarios = numero_funcionarios

    # 4° Membro
    def calcular_imposto(self) -> float:
        renda = self._renda_anual
        
        aliquota = 0.14 if self._numero_funcionarios > 10 else 0.16
            
        return renda * aliquota
# Fim de Sub Classe PessoaJuridica

# Modulo - Saida de Dados

def ler_float(clodoaldo: str) -> float:
    while True:
        try:
            return float(input(clodoaldo).replace(',', '.'))
        except ValueError:
            print("Entrada invalida. Digite um namero.")

def ler_int(clodoaldo: str) -> int:
    while True:
        try:
            num = int(input(clodoaldo))
            if num < 0:
                raise ValueError
            return num
        except ValueError:
            print("Entrada inválida. Digite um número inteiro não negativo.")

def main():
    print("--- Sistema de Cálculo de Imposto ---")

    N = ler_int("Quantos contribuintes cadastrar? ")

    lista_contribuintes = []

    for i in range(1, N + 1):
        print(f"\n Contribuinte {i}/{N} ")
        
        while True:
            tipo = input("Tipo (PF/PJ): ").upper()
            if tipo in ['PF', 'PJ']:
                break
            print("Tipo inválido. Digite 'PF' ou 'PJ'.")
            
        nome = input("Nome: ")
        renda = ler_float("Renda Anual (R$): ")

        try:
            if tipo == 'PF':
                gastos_saude = ler_float("Gastos com Saúde (R$): ")
                contribuinte = PessoaFisica(nome, renda, gastos_saude)
            else:
                num_funcionarios = ler_int("Número de Funcionários: ")
                contribuinte = PessoaJuridica(nome, renda, num_funcionarios)
            
            lista_contribuintes.append(contribuinte)
            
        except ValueError as e:
            print(f"Erro no cadastro: {e}. Repita o cadastro.")
            i -= 1 

    print("\n" + "="*40)
    print("RESUMO DOS IMPOSTOS")
    print("="*40)

    total_arrecadado = 0.0

    for c in lista_contribuintes:
        imposto = c.calcular_imposto()
        total_arrecadado += imposto
        print(c.exibir_dados())

    print("-" * 40)
    print(f"TOTAL TAXADO: R$ {total_arrecadado:,.2f}")
    print("="*40)

if __name__ == "__main__":
    main()