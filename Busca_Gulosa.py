from VetorOrdenado import VetorOrdenado
from VetorOrdenadoAdjacente import VetorOrdenadoAdjacente

class Buscagulosa:
    rota = ""
    custo = 0   
    
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print("\nAtual: {}\nMeus adjacentes são:" .format(atual.nome))
        atual.visitado = True
        Buscagulosa.rota += atual.nome
        

        if atual == self.objetivo:
            self.achou = True
            print("Minha rota foi: {}" .format(Buscagulosa.rota))
            print("Meu custo foi: {}" .format(Buscagulosa.custo))
        else: 
            self.fronteira = VetorOrdenado(len(atual.adjacentes))
            self.fronteira_adjacentes = VetorOrdenadoAdjacente(len(atual.adjacentes))
            for i in atual.adjacentes:

                if i.cidade.visitado == False:
                    i.cidade.visitado = True
                    self.fronteira.inserir(i.cidade)   
                    self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                Buscagulosa.custo += i.distancia

            if self.fronteira.getPrimeiro() != None:
                
                Buscagulosa.buscar(self, self.fronteira.getPrimeiro())
        

cidadeInicial = input("Escolha o Nó inicial, com uma letra maiuscula ")
from Mapa import Mapa
mapa = Mapa()
gulosa = Buscagulosa(mapa.M) 
if cidadeInicial == 'A': 
            gulosa.buscar(mapa.A)
elif cidadeInicial == 'B': 
            gulosa.buscar(mapa.B)
elif cidadeInicial == 'C': 
            gulosa.buscar(mapa.C)
elif cidadeInicial == 'D': 
            gulosa.buscar(mapa.D)
elif cidadeInicial == 'E': 
            gulosa.buscar(mapa.E)
elif cidadeInicial == 'F': 
            gulosa.buscar(mapa.F)
elif cidadeInicial == 'G': 
            gulosa.buscar(mapa.G)
elif cidadeInicial == 'H': 
            gulosa.buscar(mapa.H)
elif cidadeInicial == 'I': 
            gulosa.buscar(mapa.I)
elif cidadeInicial == 'J': 
            gulosa.buscar(mapa.J)
elif cidadeInicial == 'K': 
            gulosa.buscar(mapa.K)
elif cidadeInicial == 'L': 
            gulosa.buscar(mapa.L)
elif cidadeInicial == 'M': 
            gulosa.buscar(mapa.M)
elif cidadeInicial != "":
    print("Não é um Nó valido")