from enum import Enum

class Estados_Pedidos(Enum):
    AGUARDANDO_PAGAMENTO = 0
    PROCESSANDO = 1
    ENVIADO = 2
    ENTREGUE = 3
    CANCELADO = 4

# Exemplo de Uso 
print(Estados_Pedidos(2))
print(Estados_Pedidos.CANCELADO)
print(Estados_Pedidos.ENVIADO.name)
print(Estados_Pedidos.ENTREGUE.value)
print(Estados_Pedidos(1).name)
