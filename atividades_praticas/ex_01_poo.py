class Spotify:
    musicas = []
    def __init__(self, nome, artista, categoria, duracao):
        self.nome = nome
        self.artista = artista
        self.categoria = categoria
        self.duracao = duracao
        Spotify.musicas.append(self) # Adiciona a instância à lista de músicas

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.categoria} | {self.duracao} segundos'

    def play():
        for musica in Spotify.musicas:
            print(f'Tocando: {musica.nome} de {musica.artista} [ {musica.duracao} segundos]')

musica1 = Spotify('Umbrella', 'Rihanna', 'Pop', 240)
musica2 = Spotify('Flowers', 'Miley Cyrus', 'Pop', 200)
musica3 = Spotify('Calm Down', 'Rema', 'Afrobeat', 210)
Spotify.play()


# EX - 02 - POO
class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def carro_info():
        for carro in Carro.carros:
            print(f'Modelo: {carro.modelo} | Cor: {carro.cor} | Ano: {carro.ano}')

mustang = Carro('Ford Mustang', 'Vermelho', 2020)
camaro = Carro('Chevrolet Camaro', 'Preto', 2019)
Carro.carro_info()

# EX - 03 - POO
class Cliente:
    clientes = []
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        Cliente.clientes.append(self)

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'Nome: {cliente.nome} | Idade: {cliente.idade} | Email: {cliente.email}')

cliente1 = Cliente('Ana', 28, 'ana@email.com')
cliente2 = Cliente('Bruno', 35, 'bruno@hotmail.com')

Cliente.listar_clientes()