from random import random

class Produto():
    def __init__(self, nome, valor, peso):
        self.nome = nome
        self.valor = valor
        self.peso = peso

if __name__ == '__main__':
    lista_produtos = []
    lista_produtos.append(Produto("Ventilador", 15.50, 10.132))
    lista_produtos.append(Produto("Barraca", 90.60, 40.156))
    lista_produtos.append(Produto("Cooler", 50.10, 26.567))
    lista_produtos.append(Produto("Mochila", 60.25, 32.389))
    lista_produtos.append(Produto("Fogareiro", 12.82, 8.753))
    lista_produtos.append(Produto("Material de Pesca", 89.75, 12.589))
    lista_produtos.append(Produto("Comida", 250.75, 42.39))
    for produto in lista_produtos:
        print("Nome: " + str(produto.nome) + " Valor: " + str(produto.valor) + " Peso: " + str(produto.peso))
