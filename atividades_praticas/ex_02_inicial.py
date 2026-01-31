# Exercício 1: Classificação de Música
def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Rock', 'Pop')
print(resultado)

# Exercício 2: Configuração de Tempo de Foco
def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco desejado em minutos: "))
    if 25 <= tempo <= 45:
        print ("Tempo de foco configurado para", tempo, "minutos.")
    else:
        print ("Tempo inválido. Por favor, escolha um valor entre 25 e 45 minutos.")

configurar_tempo_foco()
