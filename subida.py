from individuo import Individuo
import random

class subida:
    def __init__(self, it_max):
          self.it_max = it_max
          self.atual = []
          self.last_id = -1

    def estado_inicial(self):
        """
        funcao que gera um estado inicial aleatorio
        """
        r_ind = []
        for i in range(8):
            r_ind.append(random.randint(0,7))
        return r_ind

    def aga(self, ind):
        """
        funcao de minimizacao h(x)
        que calcula quantos pares de rainhas estao se atacando
        """
        attack = 0
        j = 0
        for k in range(0,8):
            for i in range (k+1,8):
                print(ind[k],ind[i]+(i-k))
                # Verifica se existem pares na mesma linha horizontal
                if ind[k] == ind[i]:
                    attack = attack + 1
                # Verifica se na mesma diagonal inferior
                if ind[k] == ind[i]-(i-k):
                    attack = attack + 1
                # Verifica se na mesma diagonal superior
                if ind[k] == ind[i]+(i-k):
                    attack = attack + 1
                j+=1
        print(j)
        return attack
    
    def melhor_sucessor(self, ind):
        """
        encontra todos os sucessores do estado atual
        e dentre eles calcula qual o que possui o menor número h(x)
        por enquanto incompleta
        """
        melhor = ind.copy
        aux = []
        for i in range(8):
            for j in range(8):
                aux = ind.copy
                aux[i] = j
                if self.aga(aux) >= self.aga(melhor):
                    melhor = aux.copy
        return melhor

    def imprimir_tabuleiro(self, atual):
        print('---------------------------------------')
        print(atual)
        print('---------------------------------------')

    def imprimir_aga(self, atual):
        funcao = self.aga(atual)
        print('---------------------------------------')
        print('O numero de individuos que nao se atacam eh: ' + funcao)
        print('---------------------------------------')

    def subida_encosta(self):
        """
        funcao principal
        """
        self.atual = self.estado_inicial()
        print('Estado inicial aleatorio: ')
        self.imprimir_tabuleiro(self.atual)
        it = 1
        vizinho = []
        while it <= self.it_max:
            vizinho = self.melhor_sucessor(self.atual)
            if self.aga(vizinho) <= self.aga(self.atual):
                self.atual = vizinho.copy
            it = it + 1
        self.imprimir_tabuleiro(self.atual)
        self.imprimir_aga(self.imprimir_aga)