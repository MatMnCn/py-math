import produtoOOP as p #Importar o Modulo 
p1 = p.Produto() #Instanciar o objeto
# Entrada de Dados
print("Digite os Dados do Produto:")
p1.nome = input ("\tNome: ")
p1.saldo = int(input("\Quantidade: "))
# Saida de dados 1
print ("Dados do Produto")
print (f"\tNome do Produto: {p1.nome}")
print (f"\tValor de compra: R$ {p1.preco}")
print (f"\tQuantidade em Estoque: {p1.saldo}")
print (f"\tValor Total em Estoque: R$ {p1.valorTotalEmEstoque()}")