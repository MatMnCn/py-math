import produtoOOP as p 

# Entrada de Dados
print("Entre com os dados do produto:")
nome = input ("Nome: ")
preco = int(input("Preço: R$"))
saldo = int(input("Quantidade: "))

# Instanciar o meu objeto
# ps = p.Produto(nome, preco, saldo)
ps = p.Produto(nome, preco)

# Saída de Dadosh
print(ps.dadosDoProduto())