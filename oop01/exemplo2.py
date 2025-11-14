import produtoOOP as p #Importar o Modulo 
p1 = p.Produto() #Instanciar o objeto
# Entrada de Dados
print("Digite os Dados do Produto:")
p1.nome = input ("\tNome: ")
p1.preco = float(input("\tpreço: R$"))
p1.saldo = int(input("\Quantidade: "))
# Saida de dados 1
print ("Dados do Produto")
# Adicionar Produtos
q = int(input("Digite o número de produtos a ser adicionado ao estoque: "))
p1.adicionarProdutos(q)
# Saída de Dados 2
print("--Dados Atualizados--")
print(p1.dadosDoProduto())
# Remover Produtos
q = int(input("Digite o número de produtos a ser removido ao estoque: "))
p1.removerProdutos(q)
# Saida de Dados 3
print("--Dados atualizado--")
print(p1.dadosDoProduto())