#Lucas Salame e Matthews Gonçalves
import sys
import os

print ("""Programa de Buscas em Malha de Nós de A até M com objetivo M
1.Busca Gulosa\n
2.Busca A estrela\n
""")

encerra = 0

while encerra == 0:
      
  ans = input("Qual tipo de busca? ") 

  if ans == "1": 
    print("\n Busca Gulosa")
    from Busca_Gulosa import Buscagulosa
    input("\n\nPressione Enter para encerrar")
    os.system("cls")
    encerra = 1

  elif ans == "2":
    print("\n Busca A estrela") 
    from Busca_AEstrela import BuscaAEstrela
    input("\n\nPressione Enter para encerrar")
    os.system("cls")
    encerra = 1

  elif ans != "":
    print("\n Não é uma entrada valida")
    input("\n\nPressione Enter para reiniciar")
    os.system("cls")
