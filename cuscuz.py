print("cuscuz")


def salvar_contatos(lista):
    arquivo = open("contatos.txt", "w")

    for contato in lista:
        arquivo.write("{}:{}:{}:{}:{}\n".format(contato['nome'], contato['email'], contato['telefone'], contato['endereço'], contato['classificação']))

    arquivo.close()


def existe_contato(lista, email):
    if len(lista) > 0:
       for contato in lista:
           if contato['email'] == email:
              return True
        
    return False


def Criar(lista) :

    while True:
        email = input("Digite o e-mail do contato:  ")

        if not existe_contato(lista, email):
            break
        else:
            print("Esse e-mail já foi utilizado.")
            print("Por favor, digite outro e-mail.")

 # Nessa parte aí, ta colocando o email único do contato, nenhum outro tem igual.

    contato = {
        "E-mail" : email,
        "Nome" : input("Digite o nome do contato: "),
        "Telefone" : input("Digite o telefone do seu contato: "),
        "Classificação" : input("Digite a classificação do seu contato (contatinho, trabalho e pessoal): "),
        "Endereço": input("Digite o endereço do contato: ")
    }

    lista.append(contato)

    print("O contato {} foi salvo!!\n".format(contato['nome']))

def Abrir():
    pass

def Editar():
    pass

def Excluir():
    pass

def Listar_contatos():
    pass

def Salvar():
    pass

def Fechar():
    pass

def principal():

 lista = []   #Essa lista é onde os contatos são armazenados, inicialmente ela está vazia.

 while True:
    print("------- Agenda telefônica -------")
    print(" 1 - Abrir agenda")
    print(" 2 - Criar contato")
    print(" 3 - Editar contato")
    print(" 4 - Excluir contato")
    print(" 5 - Listar contatos existentes")
    print(" 6 - Salvar agenda")
    print(" 7 - Fechar Agenda")
    print(" 8 - Sair")
    opção = int(input("> "))

    if opção == 1:
        Abrir()
    elif opção == 2:
        Criar(lista)
        salvar_contatos(lista)
    elif opção == 3:
        Editar()
        salvar_contatos(lista)
    elif opção == 4:
        Excluir()
        salvar_contatos(lista)
    elif opção == 5:
        Listar_contatos(lista)
    elif opção == 6:
        Salvar()
        salvar_contatos(lista)
    elif opção == 7:
        Fechar()
        salvar_contatos(lista)
    elif opção == 8:
        print("Tchau tchau..")
        break
    else:
        print("Opção inexistente, tente outra.")