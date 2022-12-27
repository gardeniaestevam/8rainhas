from genetico import Genetico
from individuo import Individuo
from subida import subida

#menuzinho em construção
#não sei se seria legal porque a gente teria que tratar o que está entrando

while True:
    print('O que voce deseja fazer?')
    opcao = int(input('Digite 1 para Algoritmo Genetico ou 2 para subida na encosta e 3 para sair: '))

    match opcao:
        case 1:
            print('Você escolheu Algoritmo Genetico')
            it_max1 = int(input('Digite o numero maximo de iteracoes: '))
            tam_pop = int(input('Digite o tamanho da populacao: '))
            tx_mut = float(input('Digite o numero da taxa de mutacao: '))
            gen = Genetico(it_max1, tam_pop, tx_mut)
            gen.alg_genetico()
            opcao1 = int(input('Digite 1 para sair ou qualquer coisa para retornar ao menu principal: '))
            match opcao1:
                case 1:
                    break
                case _:
                    continue
        case 2:
            print('Você escolheu Subida na Encosta')
            it_max2 = int(input('Digite o numero maximo de iteracoes: '))
            resultado = subida(it_max2)
            resultado.subida_encosta()
            opcao1 = int(input('Digite 1 para sair ou qualquer outro numero para retornar ao menu principal: '))
            match opcao1:
                case 1:
                    break
                case _:
                    continue
        case 3:
            break
        case _:
            print('Desculpa, você não digitou algo correspondente às nossas opções.')