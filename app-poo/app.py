from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('Pizzaria Guston', 'Italiana')
restaurante_sushi = Restaurante('Sushi Ozaka', 'Japonesa')
restaurante_hamburguer = Restaurante('Burger House', 'Fast Food')

restaurante_hamburguer.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()