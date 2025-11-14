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
    def dadosDoProduto (self) -> str:

        saida = f'''
            Dados do Produto:
            \tNome do Produto: {self.nome}
            \tValpr de Compra do Produto: R$ {self.preco}
            \tQuantidade em estoque: {self.saldo}
            \tValor Total em Estoque: R$ {self.valorTotalEmEstoque():.2f}
            '''
        return saida