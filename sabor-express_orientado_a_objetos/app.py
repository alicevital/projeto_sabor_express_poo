from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Carlos', 10)
restaurante_praca.receber_avaliacao('Bia', 10)
restaurante_praca.receber_avaliacao('Allan', 7)
restaurante_praca.receber_avaliacao('Thiago', 6)
restaurante_praca.receber_avaliacao('Alice', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()