from Cidade import Cidade
from Adjacente import Adjacente

class Mapa:
    A = Cidade("A", 223)
    B = Cidade("B", 222)
    C = Cidade("C", 166)
    D = Cidade("D", 192)
    E = Cidade("E", 165)
    F = Cidade("F", 136)
    G = Cidade("G", 122)
    H = Cidade("H", 111)
    I = Cidade("I", 100)
    J = Cidade("J", 60)
    K = Cidade("K", 32)
    L = Cidade("L", 102)
    M = Cidade("M", 0)

    A.addCidadeAdjacente(Adjacente(B, 36))
    A.addCidadeAdjacente(Adjacente(C, 61))

    B.addCidadeAdjacente(Adjacente(A, 36))
    B.addCidadeAdjacente(Adjacente(D, 31))

    C.addCidadeAdjacente(Adjacente(A,61))
    C.addCidadeAdjacente(Adjacente(D,32))
    C.addCidadeAdjacente(Adjacente(F,31))
    C.addCidadeAdjacente(Adjacente(L,80))

    D.addCidadeAdjacente(Adjacente(B, 31))
    D.addCidadeAdjacente(Adjacente(C, 32))
    D.addCidadeAdjacente(Adjacente(E, 52))

    E.addCidadeAdjacente(Adjacente(D, 52))
    E.addCidadeAdjacente(Adjacente(G, 43))

    F.addCidadeAdjacente(Adjacente(C, 31))
    F.addCidadeAdjacente(Adjacente(J, 122))
    F.addCidadeAdjacente(Adjacente(K, 112))

    G.addCidadeAdjacente(Adjacente(E, 43))
    G.addCidadeAdjacente(Adjacente(H, 20))

    H.addCidadeAdjacente(Adjacente(G, 20))
    H.addCidadeAdjacente(Adjacente(I, 40))

    I.addCidadeAdjacente(Adjacente(H, 40))
    I.addCidadeAdjacente(Adjacente(J, 45))

    J.addCidadeAdjacente(Adjacente(I, 45))
    J.addCidadeAdjacente(Adjacente(F, 122))
    J.addCidadeAdjacente(Adjacente(K, 36))

    K.addCidadeAdjacente(Adjacente(J, 36))
    K.addCidadeAdjacente(Adjacente(F, 112))
    K.addCidadeAdjacente(Adjacente(M, 32))

    L.addCidadeAdjacente(Adjacente(C, 80))
    L.addCidadeAdjacente(Adjacente(M, 102))

    M.addCidadeAdjacente(Adjacente(L, 102))
    M.addCidadeAdjacente(Adjacente(K, 32))