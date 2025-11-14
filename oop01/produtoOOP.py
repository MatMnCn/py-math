class Produto:
    # Atributos
    nome:str
    preco:float
    quantidade:int
    # Metodos
    def valorTotalEmEstoque(self) -> float:
        return self.preco * self.saldo
    def adicionarProdutos(self, quantidade) -> int:
        self.saldo = quantidade + self.saldo
        return self.saldo
    def removerProdutos(self, quantidade) -> int:
        self.saldo = self.saldo - quantidade