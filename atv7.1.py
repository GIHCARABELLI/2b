# alunos = []
# notas = []

# concluir = False

# while (not concluir):
#     print("Digite o nome do aluno:")
#     nomeAluno = input()
#     print("Digite a nota do aluno")
#     notaAluno = int(input())

#     if(notaAluno < 5): print("Misericórdia")
#     elif(notaAluno < 7): print("Tá quase")
#     else: print("Passsssssou")

#     alunos.append(nomeAluno)
#     notas.append(notaAluno)

#     print("Deseja inserir outra nota?(s/n)")
#     concluir = input() == "n"

# print("Seguem abaixo todas as notas digitadas:")
# print("Aluno : Nota")
# for i in range(len(alunos)):
#     print(f"{alunos[i]} : {notas[i]}")

# input("Pressione Enter pra terminar...")


produto = []
preço = []
quantidade = []

concluir = False

while (not concluir):
    print("digite o nome do produto:")
    nomeProduto = input()
    print("digite o valor do produto:")
    preçoProduto = float(input())
    print("digite a quantidade do produto:")
    quantidadeProduto = int(input())

    produto.append(nomeProduto)
    preço.append(preçoProduto)
    quantidade.append(quantidadeProduto)

    print("deseja adicionar outra nota?(s/n)")
    concluir = input() == "n"

print("segue a tabela abaixos:")

print("produto : preço : quantidade")

for i in range(len(produto)):
    print(f"{produto[i]} : {preço[i]} : {quantidade[i]}")

input("pressione Enter para continuar")

import os

filename = "tabelaDoArcoMix.txt"
file = open(filename, 'w')

file.write("Se liga nas promo de hoje\n")
file.write("produto : preço : quantidade\n")

for i in range(len(produto)):
    outputline = f"{produto[i]} : {preço[i]} : {quantidade[i]}\n"
    file.write(outputline)

file.write("Cabou")

file.close()


os.system(f"notepad {filename}") 