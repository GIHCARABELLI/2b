# ALUNAS: Giovanna Carabelli e Lara Dayane





# escreva um programa em python que:

# 1: receba um numero inteiro e faça uma contagem regressiva;

# 2: receba um numero inteiro e calcule a soma recursiva até 1;

# 3: receba uma string e retorne a string invertida.

# ------------------------------------

import time 

# def fatorial (i : int):

#     num = int(input("Digita um número inteiro ai po: "))
#     for i in range(num,  0,  -1):
#         print(i)
#     print("Acabou a conatgem, sai fora!")


# # def countdown(number):
# #     for i in range(number, 0, -1):
# #         print(i)
# #         time.sleep(1)
# #     print("contagem regressiva concluída!")   
    
def contagemregressiva(i : int ):
    if(i <= 0): print(0)
    else:
        time.sleep(1)
        print(i)
        contagemregressiva(i-1)

print("contagem regressiva de 10:")       
contagemregressiva(10)

def somaRecursiva (i: int):
    if( i <= 1): return 1
    else: 
         return  i + somaRecursiva(i-1)
    
print("soma recursiva")    
print(f"de 1: {somaRecursiva(1)}")
print(f"de 2: {somaRecursiva(2)}")
print(f"de 3: {somaRecursiva(3)}")
print(f"de 4: {somaRecursiva(4)}")
print(f"de 5: {somaRecursiva(5)}")
print(f"de 6: {somaRecursiva(6)}")
print(f"de 7: {somaRecursiva(7)}")
print(f"de 8: {somaRecursiva(8)}")
print(f"de 9: {somaRecursiva(9)}")
print(f"de 10: {somaRecursiva(10)}")


#  1° Exercicio

def potencia(base, expoente):
    if expoente == 0: return 1
    else: return base * potencia(base, expoente - 1)

print(f" 2 elevado a 2: {potencia(2, 2)}") 
print(f" 2 elevado a 3: {potencia(2, 2)}") 
print(f" 3 elevado a 2: {potencia(2, 2)}") 
print(f" 3 elevado a 3: {potencia(2, 2)}") 


# 3° Exercicio

def inverter_string(s):
    if len(s) == 0: return ""
    else: return s[-1] + inverter_string(s[:-1])

print("inverter strings")
print(f'recursividade : {inverter_string("recursividade")}')
print(f'subir no ônibus : {inverter_string("subir no ônibus")}')
print(f'paçoca : {inverter_string("paçoca")}')
print(f'bombom : {inverter_string("bombom")}')










    
    
    


