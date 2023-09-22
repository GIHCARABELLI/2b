import keyboard
import time
import os

def tela_principal(contatos):
    print("-----------Agenda Telefônica-------------")




def Esperar_tecla(ValidarTeclas):
    while True:
        Key_pressed = keyboard.read_key()
        if(Key_pressed != ""):
            if(len(ValidarTeclas) == 0):
               return Key_pressed
            if(Key_pressed in ValidarTeclas):
                return Key_pressed
        time.sleep(0.3)    

def selecionar_tipo_contato():
    time.sleep(1)
    print("Selecione o tipo do contato: ")
    print("0 -> Pessoal")
    print("1 -> Profissional")
    print("2 -> Contatinho")
    Tipo = Esperar_tecla([0, 1, 2])
    time.sleep(1)
    return Tipo

Tipo = ["Pessoal", "Profissional", "Contatinho"]

contatos = []


def criar_contatos( Número, Nome, Telefone, Endereço, ):
    contato = {}
    contato ['Nome'] = Nome
    contato ['Número'] = len(contatos)
    contato ['Endereço'] = Endereço
    contato ['Tipo'] = Tipo
    

def preencher_formulario(Contatos):
    print(" Insira um nome para contato: ")
    Nome = input("Digite o nome do seu contato: ")
    Telefone = input("Digite o telefone do seu contato: ")
    Endereço = input(" Digite o endereço do seu contato: ")
   

    Número = len(contatos)
    novo_contato = criar_contatos( Número, Nome, Telefone, Endereço)
    return novo_contato

def inserir_contato(Contatos):    ...

def remover_contato_por_nome(contatos, nome, nomeNovo, Telefone, Endereço, Tipo):
    for contato in contatos:
        if(contato["Nome"] == nome):
            contato["Nome"] = nomeNovo
            contato["Telefone"] = Telefone
            contato["Endereço"] = Endereço
            contato["Tipo"] = Tipo
    return contatos        

def remover_contato_por_telefone(contatos, telefone):
    contatos_mantidos = []    
    for contato in contatos:
        if(contato["Telefone"] != telefone):
            contatos_mantidos.append(contato)
        else: 
            print(f"Contato Excluido: []")    

def criar_contato(nome, telefone, e-mail, endereço, classificação):
    contato = {}
    contato ['Nome']
    contato ['Número'] = len(contatos)
    contato ['Endereço']


