# Lista em python
lista = ["Senai", True, 22, 3.5 ]
print(lista)
print(type(lista))
print(lista[2])
print(len(lista))
lista.insert(1,"Campeão")
lista.append("Feriado")
del lista [3]
lista.append ("Senai")
for i in range (len(lista)):
    print(lista[i])

# Tupla

tupla = ("Senai", True, 56, 74.6)
print(tupla)
print (type(tupla))
print(tupla[3])
print(tupla[1])
# tupla.insert(1, "Campeão")
del tupla[1]
TUPLA = ("Senai", True, 56, 74.6)

# Dicionario

dicionario = {"nome": "Senai", "lógica": False, "num1": 2, "num2": 1.5 }
print(dicionario)
print(type(dicionario))
print(dicionario["lógica"])
for chave in dicionario.keys():
    print (chave, "-->", dicionario[chave])
dicionario.update({"novo":"Senai"})
dicionario.update({"nome":"Terca"})
del dicionario["lógica"]

# Conjunto

conjunto = {"Senai", False, 10, 2.69}
print(conjunto)
print(type(conjunto))
print(conjunto[2])
conjunto.add(23)
conjunto.discard("Senai")
conjunto.clear()