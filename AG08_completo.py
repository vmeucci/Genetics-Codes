from random import random
import matplotlib.pyplot as plt

class Produto():
    def __init__(self, nome, valor, peso):
        self.nome = nome
        self.valor = valor
        self.peso = peso

class Individuo():
    def __init__(self, pesos, valores, limite_pesos, geracao=0):
        self.pesos = pesos
        self.valores = valores
        self.limite_pesos = limite_pesos #peso máximo (w=80 no exemplo)
        self.fitness = 0
        self.peso_total = 0
        self.geracao = geracao
        self.cromossomo = []

        for i in range(len(pesos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")

    def avaliacao(self):
        calculo_fitness = 0
        soma_pesos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                calculo_fitness += self.valores[i]
                soma_pesos += self.pesos[i]
        if soma_pesos > self.limite_pesos:
            calculo_fitness = 1 #para algoritmos geneticos, a nota (nesta caso fitness) é rebaixado para 1, assim este
                                #individuo/cromossomo acabará ficando para traz em relação aos melhores (fitness maior)
        self.fitness = calculo_fitness
        self.peso_total = soma_pesos

    def crossover(self, individuo):
        corte = round(random() * len(self.cromossomo))
        filho1 = individuo.cromossomo[0:corte] + self.cromossomo[corte:]
        filho2 = self.cromossomo[0:corte] + individuo.cromossomo[corte::]
        filhos = [Individuo(self.pesos, self.valores, self.limite_pesos, self.geracao+1),
                  Individuo(self.pesos, self.valores, self.limite_pesos, self.geracao+1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos

    def mutacao(self, taxa_mutacao):
        print("Antes...%s" % self.cromossomo)
        for i in range(len(self.cromossomo)):
            escolha = random()
            #print("Escolha: %s" % escolha)
            if escolha < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        print("Depois..%s\n" % self.cromossomo)
        return self

class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []

    def inicializa_populacao(self, pesos, valores, limite_peso):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(pesos, valores, limite_peso))
        self.melhor_solucao = self.populacao[0]

    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.fitness,
                                reverse = True)

    def melhor_individuo(self, individuo):
        if individuo.fitness > self.melhor_solucao.fitness:
            self.melhor_solucao = individuo

    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.fitness
        return soma

    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].fitness
            pai += 1
            i += 1
        return pai

    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print("G:%s -> Valor: %s Peso: %s Cromossomo: %s" % (self.populacao[0].geracao,
                                                               melhor.fitness,
                                                               melhor.pesos,
                                                               melhor.cromossomo))

    def resolver(self, taxa_mutacao, numero_geracoes, pesos, valores, limite_peso):
        self.inicializa_populacao(pesos, valores, limite_peso)

        for individuo in self.populacao:
            individuo.avaliacao()

        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.fitness)

        self.visualiza_geracao()

        for geracao in range(numero_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []

            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)

                filhos = self.populacao[pai1].crossover(self.populacao[pai2])

                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))

            self.populacao = list(nova_populacao)

            for individuo in self.populacao:
                individuo.avaliacao()

            self.ordena_populacao()

            self.visualiza_geracao()

            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.fitness)
            self.melhor_individuo(melhor)

        print("\nMelhor solução -> G: %s Valor: %s Peso: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.fitness,
               self.melhor_solucao.pesos,
               self.melhor_solucao.cromossomo))

        return self.melhor_solucao.cromossomo

if __name__ == '__main__':
    lista_produtos = []
    lista_produtos.append(Produto("Ventilador", 15.55, 10.132))
    lista_produtos.append(Produto("Barraca", 90.64, 40.156))
    lista_produtos.append(Produto("Cooler", 50.12, 26.567))
    lista_produtos.append(Produto("Mochila", 60.25, 32.389))
    lista_produtos.append(Produto("Fogareiro", 12.82, 8.753))
    lista_produtos.append(Produto("Pescaria", 89.75, 12.589))
    lista_produtos.append(Produto("Comida", 250.75, 42.39))
    '''
    print("LISTA DE PRODUTOS")
    for produto in lista_produtos:
        print("Produto: " + str(produto.nome) + " | Valor: " + str(produto.valor) + " | Peso: " + str(produto.peso))
    print("\n")
    '''
    pesos = []
    valores = []
    nomes = []
    for produto in lista_produtos:
        pesos.append(produto.peso)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    limite = 110

    tamanho_populacao = 50
    taxa_mutacao = 0.01
    numero_geracoes = 100
    objAlgoritmoGenetico = AlgoritmoGenetico(tamanho_populacao)
    resultado = objAlgoritmoGenetico.resolver(taxa_mutacao, numero_geracoes, pesos, valores, limite)
    for i in range(len(lista_produtos)):
        if resultado[i] == '1':
            print("Produto: %s \t| Valor: R$ %s \t| Peso: %s" % (lista_produtos[i].nome,
                                       lista_produtos[i].valor,
                                       lista_produtos[i].peso))

    # for valor in ag.lista_solucoes:
    #    print(valor)
    plt.plot(objAlgoritmoGenetico.lista_solucoes)
    plt.title("Acompanhamento dos valores")
    plt.show()



