# Exercício 3: Verificar se um número é par ou ímpar
def verificar_par_impar():
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

verificar_par_impar()

# Exercício 4: Classificar idade
def classificar_idade():
    idade = int(input("Digite a sua idade: "))
    if 0 <= idade <= 4:
        print("Bebê")
    elif 5 <= idade <= 12:
        print("Criança")
    elif 13 <= idade <= 18:
        print("Adolescente")
    else:
        print("Adulto")

classificar_idade()

import getpass

# # Exercicio 5: Verificar login e senha
def verificacao_de_login():
    login_usuario = 'admin'
    senha_usuario = 'senha123'

    login_input = input("Login: ")
    senha_input = getpass.getpass("\nSenha: ")

    if login_input == login_usuario and senha_input == senha_usuario:
        print("\nLogin realizado com sucesso")
    else:
        print("Usuário ou senha inválidos")

verificacao_de_login()

# Exercicio 6: Solicitar coordenadas plano cartesiano
def solicitar_coordenadas():
    x = int(input("\nDigite o primeiro valor x: "))
    y = int(input("\nDigite o segundo valor y: "))

    if x > 0 and y > 0:
        print("\nO ponto está no primeiro quadrante\n")
    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante\n")
    elif x > 0 and y > 0:
        print("O ponto está no terceiro quadrante\n")
    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante\n")
    else:
        print("O ponto está no eixo origem")

solicitar_coordenadas()