from random import random

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
        print("\nAntes...%s" % self.cromossomo)
        for i in range(len(self.cromossomo)):
            escolha = random()
            #print("Escolha: %s" % escolha)
            if escolha < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        print("Depois..%s" % self.cromossomo)
        return self

if __name__ == '__main__':
    lista_produtos = []
    lista_produtos.append(Produto("Ventilador", 15.50, 10.132))
    lista_produtos.append(Produto("Barraca", 90.60, 40.156))
    lista_produtos.append(Produto("Cooler", 50.10, 26.567))
    lista_produtos.append(Produto("Mochila", 60.25, 32.389))
    lista_produtos.append(Produto("Fogareiro", 12.82, 8.753))
    lista_produtos.append(Produto("Material de Pesca", 89.75, 12.589))
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
    limite = 80

    individuo1 = Individuo(pesos, valores, limite)
    print("\nIndividuo 1")
    print("Cromossomo = %s" % str(individuo1.cromossomo))
    for i in range(len(lista_produtos)):
        if individuo1.cromossomo[i] == '1':
            print("Produto: %s | Valor: R$ %s " % (lista_produtos[i].nome, lista_produtos[i].valor))
    individuo1.avaliacao()
    print("Fitness    = %s" % individuo1.fitness)
    print("Peso Total = %s" % individuo1.peso_total)

    individuo2 = Individuo(pesos, valores, limite)
    print("\nIndividuo 2")
    print("Cromossomo = %s" % str(individuo2.cromossomo))
    for i in range(len(lista_produtos)):
        if individuo2.cromossomo[i] == '1':
            print("Produto: %s | Valor: R$ %s " % (lista_produtos[i].nome, lista_produtos[i].valor))
    individuo2.avaliacao()
    print("Fitness    = %s" % individuo2.fitness)
    print("Peso Total = %s" % individuo2.peso_total)

    individuo1.crossover(individuo2)

    individuo1.mutacao(0.05)
    individuo2.mutacao(0.05)