import os
import random
from colorama import Fore, Back

# os = limpar tela
# random = números aleatórios
# colorama = cores
# fore = cor de texto
# back = cor de fundo

jogar_novamente = "s"
jogadas = 0 # serve pra contar o número de jogadas em geral de uma partida
quem_joga = 1 # determina qual jogador é você, o jogador 2 é a IA
max_jogadas = 9
vitoria = "n" #no começo ela vai ser dada como não
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    
] # essa aqui é nossa matriz do jogo, 3 colunas e 3 linhas, 9 posições.


def tela():
   global velha
   os.system("cls")
   print("    0   1   2") # colunas do jogo.
   print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2]) # desenho do jogo e posição, buscando a matriz, e assim fazendo uma linha.
   print("   -----------") # linhas horizontais da velha.
   print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2]) 
   print("   -----------")
   print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2]) 
   print("Jogadas: " + Fore.LIGHTMAGENTA_EX + str(jogadas) + Fore.RESET) # esse reset é só para ficar a cor do números, sem afetar o resto do texto.

def jogador_joga():
   global jogadas
   global quem_joga
   global vitoria
   global max_jogadas
   if quem_joga == 1 and jogadas < max_jogadas:
        l = int(input("Linha..: "))
        c = int(input("Coluna.:"))
        try:
            while velha[l][c] == " ":
              velha[l][c] = "X"
              quem_joga = 2
              jogadas+= 1
        except: 
           print("Linha e/ou coluna inválida")
           os.system("pause")
           # vitoria ="n"
           
def IA_joga():
   global jogadas
   global quem_joga
   global vitoria
   global max_jogadas

   if quem_joga == 2 and jogadas < max_jogadas:
      l = random.randrange(0,3)
      c = random.randrange(0,3) 
      while velha[l][c]!= " ": 
          l = random.randrange(0,3)
          c = random.randrange(0,3) 
      velha[l][c]= "O" # isso serve para o IA jogar, sendo em ordem aleatória e um espaço vazio.
      jogadas+= 1
      quem_joga = 1

while True:
   tela()
   jogador_joga()
   IA_joga()