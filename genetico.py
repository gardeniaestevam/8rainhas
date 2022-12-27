import random
from individuo import Individuo

class Genetico:

    def __init__(self, it_max, tam_pop, tx_mut):
        self.tam_pop = tam_pop
        self.it_max = it_max
        self.tx_mut = tx_mut
        self.generation = 1
        self.last_id = -1
        self.pais = []
        self.filhos = []
        self.ngeneration = []
        self.populacao = []

    def random_ind(self):
        """
        funcao que cria um individuo aleatorio
        o id vai ser gerado a partir do id anterior
        e a geracao sera a geracao atual 
        """
        r_ind = Individuo()
        r_ind.id = self.last_id + 1
        r_ind.generation = self.generation
        for i in range(8):
            r_queen = (random.randint(0, 7))
            r_ind.board.append(r_queen)
        self.last_id = r_ind.id
        print(r_ind.board)
        return r_ind 

    def calc_fitness(self, board):
        """
        funcao fitness que conta quantos pares de rainhas nao estao se atacando
        variavel fit começa com 28, que seria o numero ideal, e para cada par que se ataca
        o valor de fit é diminuido em 1
        """
        fit = 28
        j = 0
        for k in range(0,8):
            for i in range (k+1,8):
                # Verifica se existem pares na mesma linha horizontal
                if (board[k]) == (board[i]):
                    fit = fit - 1
                # Verifica se na mesma diagonal inferior
                if board[k] == board[i]-(i-k):
                    fit = fit - 1
                # Verifica se na mesma diagonal superior
                if board[k] == board[i]+(i-k):
                    fit = fit - 1
                j+=1
        return fit

    def gera_populacao(self):
        """
        funcao responsavel por gerar uma populacao de uma dada geracao e ao final incrementa a geracao
        """
        ind = Individuo()
        for i in range(self.tam_pop):
            ind = self.random_ind()
            #ind.fitness = self.calc_fitness(ind)
            self.populacao.append(ind.board)

    def melhor_individuo(self):
        max = 0
        ind = []
        for i in range (self.tam_pop):
            ind = self.populacao[i]
            if self.calc_fitness(ind) >= max:
                max = i
        return self.populacao[i]
    
    def det_pais(self):
        """
        funcao que procura os pais da proxima geracao
        ou seja, a metade da populacao que possui os maiores fitness
        """
        aux = self.populacao.copy
        i = 1
        max = 0
        while True:
            for i in range(self.tam_pop):
                if max <= self.calc_fitness(self.aux[i]):
                    self.pais.append(self.aux[i])
                    aux.remove[i]
            i = i + 1
            if i == (self.tam_pop//2):
                break

    def mutacao(self, filho1, filho2):
        """
        funcao que realiza mutacao em dois filhos
        dada uma certa probabilidade
        """
        tx = self.tx_mut * 100
        if (random.randint(1,100)) <= tx:
            i1 = random.randint(0,7)
            filho1.board[i1] = random.randint(0, 7)
        if (random.randint(1,100)) <= tx:
            i1 = random.randint(0,7)
            filho2.board[i1] = random.randint(0, 7)

    def crossover(self, pai1, pai2):
        """
        funcao que realiza o crossver entre 2 pais e gera 2 filhos
        parte os pais em um ponto de corte aleatorio
        junta metade de um pai com a metade de outro pai e vice versa
        realiza mutacao
        e adiciona os filhos encontrados no vetor de filhos
        """
        corte = random.randint(1,6) #corte aleatorio
        filho1 = Individuo()
        filho2 = Individuo()
        filho1.id = self.last_id + 1
        filho2.id = self.last_id + 1
        self.last_id = self.last_id + 2
        filho1.generation - self.generation
        filho2.generation = self.generation
        filho1.board = pai1.board[0:corte] + pai2[corte + 1:8] #juntando as metades
        filho2.board = pai2.board[0:corte] + pai1[corte + 1:8]
        self.mutacao(filho1,filho2) #mutando os filhos
        self.filhos.append(filho1) #adicionando no vetor de filhos
        self.filhos.append(filho2)

    def add_populacao(self):
        """
        funcao que gera a nova populacao combinando os pais da populacao anteior
        com os filhos que foram gerados
        """
        self.ngeneration.append(self.pais)
        self.generation.append(self.filhos)
        self.populacao = self.ngeneration.copy

    def imprimir_melhor_individuo(self, melhor_tab):
        print('---------------------------------------')
        print("O melhor fitness encontrado foi " + self.calc_fitness(melhor_tab))
        print('---------------------------------------')
        print(melhor_tab)
        print('---------------------------------------')
    
    def alg_genetico(self):
        self.gera_populacao()
        while self.generation <= self.it_max and self.calc_fitness(self.melhor_individuo) != 28:
            self.ngeneration = None
            for i in range (self.tam_pop):
                self.pais = None
                self.det_pais()
                self.crossover()
            self.populacao = self.ngeneration.copy
            self.generation = self.generation + 1
        self.imprimir_melhor_individuo(self.melhor_individuo)