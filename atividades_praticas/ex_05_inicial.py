# EX - 01
dicionario_pessoa = {'nome': 'Ana Clara', 'idade': 25, 'cidade': 'São Paulo'}
dicionario_pessoa.update({'idade': 26})
print(dicionario_pessoa)

# # Outro método para alterar o valor de uma chave
dicionario_pessoa['idade'] = 26
print(dicionario_pessoa)


# Adicionando um novo campo ao dicionário
dicionario_pessoa.update({'profissão': 'Desenvolvedora'})
print(dicionario_pessoa)

# # Removando um campo do dicionário
dicionario_pessoa.pop('cidade')
print(dicionario_pessoa)

# # Outro método para remover um campo do dicionário
del dicionario_pessoa['idade']
print(dicionario_pessoa)

# EX - 02 
dicionario_quadrados = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(dicionario_quadrados)

# Resposta do exercício 02 na Alura:
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# Parte	Função
# range(1, 6) -> Gera números de 1 a 5
# for x in range(...) -> Percorre esses números
# {x: x**2 ...} -> Cria chave e valor no dicionário
# **2 -> Eleva ao quadrado

# EX - 03 
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")


# EX - 04
frase = "O rato roubou o isqueiro do rei de Roma"
frequencia_palavras = {}
palavras = frase.lower().split()
for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1
print(frequencia_palavras)

# Resposta do exercício 04 na Alura:
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

# Métodos utilizados no EX 04:
# - lower(): Converte todos os caracteres da string para minúsculas.
# - split(): Quebra a string em uma lista, usando um separador. Por padrão, o separador é espaço.

# O que aconteceu:
# 1.lower() → transforma tudo em minúsculo
# 2.split() → divide em palavras (Lista)
# 3.Resultado final → lista de palavras normalizadas