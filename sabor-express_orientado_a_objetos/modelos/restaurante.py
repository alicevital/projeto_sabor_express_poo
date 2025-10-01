from modelos.avaliacao import Avaliacao

class Restaurante: #nome da classe sempre maiuscula
    '''Representa um restaurante e suas caracteristicas'''

    restaurantes = []

    def __init__(self, nome, categoria): # o metodo init é o construtor usado para incializar uma instancia da classe
        '''Inicializa uma instancia de Restaurante.
        Parametros: 
        - nome (str) O nome do restaurante
        - categoria(str): A categoria do restaurante
        '''
        self._nome = nome.title() #funçao que deixa sempre com a primeira letra maiusculas
        self._categoria = categoria.upper() #funçao que deixa todas as letras maiusculas
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self): # o metodo str mostra o atributo da classe em forma de texto 'string'
        '''Retorna uma representação em string do restaurante.'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes.'''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria' .ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        '''Retorna um símbolo indicando o estado de atividade do restaurante.'''
        return 'verdadeiro ↑' if self._ativo else 'falso ↓'
    
    def alternar_estado(self):
        '''Alterna o estado de atividade do restaurante'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Registra uma avaliação para o restaurante.
        Parametros: 
        - cliente (str): O nome do cliente que fez a avaliação
        - nota (str): A nota atribuída ao restaurante(entre 1 e 5)'''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações do restaurante'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1) # o round permite arredondar o valor pelo numero que voce coloca após a vírgula
        return media


