listaprodutos = ["sprite", "paçoca", "bolodepote", "coxinha"]
listadepreco = [5, 1, 5, 5]

# for produto in listaprodutos:
#     print(produto)

# for item in listadepreco:
#     print(item)

if(len(listaprodutos) != len(listadepreco)):
    print("não dá pra fazer por que as listas tem tamanhos diferentes")
else:
    for i in range(len(listaprodutos)):
        print(f"{listaprodutos[i]} : {listadepreco[i]}")