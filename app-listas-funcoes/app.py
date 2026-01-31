import os

restaurantes = [{'id': 1, 'nome': 'Pizza Place', 'categoria': 'Italiana', 'ativo': True}, 
                {'id': 2, 'nome': 'Sushi World', 'categoria': 'Japonesa', 'ativo': True}, 
                {'id': 3, 'nome': 'Burger House', 'categoria': 'Americana', 'ativo': False}]

menu_do_restaurante_selecionado = [{'Pizza Place': {'Cardápio': ['Entradas', 'Pratos principais', 'Sobremesas']}},
                                   {'Sushi World': {'Cardápio': ['Entradas', 'Pratos principais', 'Sobremesas']}},
                                   {'Burger House': {'Cardápio': ['Entradas', 'Pratos principais', 'Sobremesas']}}]

menu_entradas_pizza_place = ['Bruschetta', 'Salada Caprese', 'Calzone']
menu_pratos_principais_pizza_place = ['Margherita', 'Pepperoni', 'Quattro Formaggi']
menu_sobremesas_pizza_place = ['Tiramisu', 'Panna Cotta', 'Gelato']

menu_entradas_sushi_world = ['Edamame', 'Sunomono', 'Gyoza']
menu_pratos_principais_sushi_world = ['Sashimi', 'Nigiri', 'Tempura']
menu_sobremesas_sushi_world = ['Mochi', 'Dorayaki', 'Anmitsu']

menu_entradas_burger_house = ['Onion Rings', 'Chicken Wings', 'Mozzarella Sticks']
menu_pratos_principais_burger_house = ['Classic Burger', 'Cheeseburger', 'Bacon Burger']
menu_sobremesas_burger_house = ['Milkshake', 'Brownie', 'Ice Cream Sundae']


def exibir_nome_do_app():
      print("""
            🆂🅰🅱🅾🆁 🅴🆇🅿🆁🅴🆂🆂 
            """)

def exibir_menu_principal():      
      print ('1. Cadastrar restaurante')
      print ('2. Listar restaurantes')
      print ('3. Ativar/Desativar restaurante')
      print ('4. Selecionar Cardápio dos restaurantes')
      print ('5. Finalizar o sistema\n')

def opcao_menu():      
      print ('1. Entradas')
      print ('2. Pratos principais')
      print ('3. Sobremesas')
      print ('4. Voltar ao menu anterior')

def finalizar_app():
      exibir_subtitulo('Finalizando o sistema...')

def voltar_ao_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal. ')
      main()

def voltar_ao_menu_anterior():
      input('\nDigite uma tecla para voltar ao menu anterior. ')
      os.system('cls')
      escolher_opcao_cardapio()

def opcao_invalida():
      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def exibir_subtitulo(subtitulo):
      os.system('cls')
      print(subtitulo)
      print()

def nome_restaurante_selecionado(nome):
      print(nome)
      
def cadastrar_novo_restaurante():
      '''Essa função é responsável por cadastrar novos restaurantes.
      
      Inputs:
      - Nome do restaurante
      - Categoria do restaurante

      Outputs:
      - Adiciona um novo restaurante à lista de restaurantes

      '''
      exibir_subtitulo('Cadastro de novos restaurantes')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
      restaurantes.append(dados_do_restaurante)
      print(f'\n O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulo('Lista de restaurantes cadastrados: ')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo_restaurante = restaurante['ativo']
            print(f'- {nome_restaurante} | {categoria_restaurante} | {ativo_restaurante}')
      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      exibir_subtitulo('Ativar/Desativar restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
      restaurante_encontrado = False
      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso!'
                  print(mensagem)

      if not restaurante_encontrado:
            print(f'\nO restaurante {nome_restaurante} não foi encontrado!')
      voltar_ao_menu_principal()

def selecionar_cardapio_pizza_place():
      exibir_subtitulo('Cardápio do Pizza Place')
      opcao_menu()
      escolher_opcao_pizza_place()

def selecionar_cardapio_sushi_world():
      exibir_subtitulo('Cardápio do Sushi World')
      opcao_menu()
      escolher_opcao_sushi_world()

def selecionar_cardapio_burger_house():
      exibir_subtitulo('Cardápio do Burger House')
      opcao_menu()
      escolher_opcao_burger_house()

def entradas_pizza_place():
      exibir_subtitulo('Entradas do Pizza Place')
      for item in menu_entradas_pizza_place:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def pratos_principais_pizza_place():
      exibir_subtitulo('Pratos principais do Pizza Place')
      for item in menu_pratos_principais_pizza_place:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def sobremesas_pizza_place():
      exibir_subtitulo('Sobremesas do Pizza Place')
      for item in menu_sobremesas_pizza_place:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def entradas_sushi_world():
      exibir_subtitulo('Entradas do Sushi World')
      for item in menu_entradas_sushi_world:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def pratos_principais_sushi_world():
      exibir_subtitulo('Pratos principais do Sushi World')
      for item in menu_pratos_principais_sushi_world:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def sobremesas_sushi_world():
      exibir_subtitulo('Sobremesas do Sushi World')
      for item in menu_sobremesas_sushi_world:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def entradas_burger_house():
      exibir_subtitulo('Entradas do Burger House')
      for item in menu_entradas_burger_house:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def pratos_principais_burger_house():
      exibir_subtitulo('Pratos principais do Burger House')
      for item in menu_pratos_principais_burger_house:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def sobremesas_burger_house():
      exibir_subtitulo('Sobremesas do Burger House')
      for item in menu_sobremesas_burger_house:
            print(f'- {item}')
      voltar_ao_menu_anterior()

def escolher_opcao_pizza_place():
      try:   
            opcao_escolhida = int(input('\nDigite a opção para abrir o cardápio do Pizza Place. '))
            # opcao_escolhida = int(opcao_escolhida)
            if opcao_escolhida == 1:
                  entradas_pizza_place()
            elif opcao_escolhida == 2:
                  pratos_principais_pizza_place()
            elif opcao_escolhida == 3:
                  sobremesas_pizza_place()
            elif opcao_escolhida == 4:
                  voltar_ao_menu_anterior()
            else:
                  opcao_invalida()
      except:
            voltar_ao_menu_principal()
      
def escolher_opcao_sushi_world():
      try:   
            opcao_escolhida = int(input('\nDigite a opção para abrir o cardápio do Sushi World: '))
            # opcao_escolhida = int(opcao_escolhida)
            if opcao_escolhida == 1:
                  entradas_sushi_world()
            elif opcao_escolhida == 2:
                  pratos_principais_sushi_world()
            elif opcao_escolhida == 3:
                  sobremesas_sushi_world()
            elif opcao_escolhida == 4:
                  voltar_ao_menu_anterior()
            else:
                  opcao_invalida()
      except:
            voltar_ao_menu_principal()

def escolher_opcao_burger_house():
      try:   
            opcao_escolhida = int(input('\nDigite a opção para abrir o cardápio do Burger House: '))
            # opcao_escolhida = int(opcao_escolhida)
            if opcao_escolhida == 1:
                  entradas_burger_house()
            elif opcao_escolhida == 2:
                  pratos_principais_burger_house()
            elif opcao_escolhida == 3:
                  sobremesas_burger_house()
            elif opcao_escolhida == 4:
                  voltar_ao_menu_anterior()
            else:
                  opcao_invalida()
      except:
            voltar_ao_menu_principal()

def escolher_opcao_cardapio():
      try:   
            exibir_subtitulo('Seleção de cardápio dos restaurantes')
            print('Restaurantes disponíveis:\n')
            for restaurante in restaurantes:
                  nome_restaurante = restaurante['nome']
                  id_restaurante = restaurante['id']
                  print(f'{id_restaurante}. {nome_restaurante}')
            print('4. Voltar ao menu principal')
            opcao_escolhida = int(input('\nSelecione o restaurante para abrir o cardápio: '))
            # opcao_escolhida = int(opcao_escolhida)

            if opcao_escolhida == 1:
                  nome_restaurante_selecionado('Pizza Place')
                  selecionar_cardapio_pizza_place()
            elif opcao_escolhida == 2:
                  nome_restaurante_selecionado('Sushi World')
                  selecionar_cardapio_sushi_world()
            elif opcao_escolhida == 3:
                  nome_restaurante_selecionado('Burger House')
                  selecionar_cardapio_burger_house()
            elif opcao_escolhida == 4:
                  voltar_ao_menu_principal()
            else:
                  opcao_invalida()
      except:
            voltar_ao_menu_principal()

def escolher_opcao_menu():
      try:   
            opcao_escolhida = int(input('Escolha uma opção: '))
            # opcao_escolhida = int(opcao_escolhida)

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  escolher_opcao_cardapio()
            elif opcao_escolhida == 5:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
      os.system('cls')
      exibir_nome_do_app()
      exibir_menu_principal()
      escolher_opcao_menu()

if __name__ == '__main__':
      main()