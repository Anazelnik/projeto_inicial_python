import os

# EX- 01
# Lista de números de 1 a 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista com quatro nomes
nomes = ["Ana", "Bruno", "Carla", "Daniel"]

# Lista com o ano que você nasceu e o atual
ano_nascimento = 1998
ano_atual = 2026

# EX- 02
elementos_das_listas = [numeros, nomes, [ano_nascimento, ano_atual]]
for lista in elementos_das_listas:
    print(lista)

# EX- 03
soma_impares = 0
for numero in range(1, 11, 2):
    soma_impares += numero
print(f"A soma dos números ímpares de 1 a 10 é: {soma_impares}")

# EX- 04
for numero in range(10, 0, -1):
    print(numero)

# EX- 05
num = int(input("Digite um numero para listar a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("\nLista da tabuada criadas com sucesso!\n")

# EX- 06
numeros_lista = [10, 20, 30, 40, 50]
soma = 0
try:
    for numero in numeros_lista:
        soma += numero
    print(f"A soma de todos os elementos da lista é: {soma}")
except Exception as e:
    print(f"Erro: {e}")

# EX- 07 
valores = [5, 10, 15, 20, 25]
try:
    media = sum(valores) / len(valores)
    print(f"A média dos valores da lista é: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Erro: {e}")