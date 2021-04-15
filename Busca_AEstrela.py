from VetorOrdenadoAdjacente import VetorOrdenadoAdjacente


class BuscaAEstrela:
    rota = ""
    custo = 0


    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print("\nAtual: {}" .format(atual.nome))
        atual.visitado = True
        BuscaAEstrela.rota += atual.nome

        if atual == self.objetivo:
            print("Objetivo {} foi alcançado. " .format(self.objetivo.nome))
            self.achou = True
            print("Minha rota foi: {}" .format(BuscaAEstrela.rota))
            print("Meu custo foi: {}" .format(BuscaAEstrela.custo))
        else:
            self.fronteira = VetorOrdenadoAdjacente(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)
                    
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                BuscaAEstrela.custo += self.fronteira.adjacentes[0].distancia
                BuscaAEstrela.buscar(self, self.fronteira.getPrimeiro())
                


cidadeInicial = input("Escolha o Nó inicial, com uma letra maiuscula ")
from Mapa import Mapa
mapa = Mapa()
aestrela = BuscaAEstrela(mapa.M)
if cidadeInicial == 'A': 
            aestrela.buscar(mapa.A) 
elif cidadeInicial == 'B': 
            aestrela.buscar(mapa.B) 
elif cidadeInicial == 'C': 
            aestrela.buscar(mapa.C) 
elif cidadeInicial == 'D': 
            aestrela.buscar(mapa.D) 
elif cidadeInicial == 'E': 
            aestrela.buscar(mapa.E) 
elif cidadeInicial == 'F': 
            aestrela.buscar(mapa.F) 
elif cidadeInicial == 'G': 
            aestrela.buscar(mapa.G) 
elif cidadeInicial == 'H': 
            aestrela.buscar(mapa.H) 
elif cidadeInicial == 'I': 
            aestrela.buscar(mapa.I) 
elif cidadeInicial == 'J': 
            aestrela.buscar(mapa.J) 
elif cidadeInicial == 'K': 
            aestrela.buscar(mapa.K) 
elif cidadeInicial == 'L': 
            aestrela.buscar(mapa.L) 
elif cidadeInicial == 'M': 
            aestrela.buscar(mapa.M) 
elif cidadeInicial != "":
    print("Não é um Nó valido")
 