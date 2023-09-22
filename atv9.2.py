# lara dayane e giovanna carabelli no dia 25/08
# declararam eterno luto pós atividade n° 9.
#  🥀

# bora lá..

import math
g = 10


def velocidadeinicial(força, massa):
    vo = força / massa
    return vo

def velocidadeinicialx(força, massa, angulo):
    vo = velocidadeinicial(força, massa)
    vox = vo * math.cos(math.radians(angulo))
    return vox

def velocidadeinicialy(força, massa, angulo):
    vo = velocidadeinicial(força, massa)
    voy = vo * math.sin(math.radians(angulo))
    return voy

def velocidadex(força, massa, angulo, tempo):
    if(tempo >= tempodevoo(força, massa, angulo)): return 0
    vox = velocidadeinicialx(força, massa, angulo)
    vx = vox
    return vox

def velocidadey(força, massa, angulo, tempo):
    if(tempo >= tempodevoo(força, massa, angulo)): return 0
    voy = velocidadeinicialy(força, massa, angulo)
    vy = voy - (g * tempo)
    return vy

def tempodevoo(força, massa, angulo):
    voy = velocidadeinicialy(força, massa, angulo)
    tmax = 2 * voy / g
    return tmax

def alcance(força, massa, angulo):
    tmax = tempodevoo(força, massa, angulo)
    vox = velocidadeinicialx(força, massa, angulo)
    xmax =  vox * tmax 
    return xmax


print("------Bora fazer esse canhão soltar bala--------")

print("---------------------------------------------------------------")

forca = float(input("Coloque a força inicial (n): "))
angulo = float(input("Coloque o ângulo de em graus(°): "))
x0 = float(input("Coloque a coordenada x (m): "))
y0 = float(input("Coloque a coordenada y  (m): "))

m = 0.5

print(f"a bala pesa {m} kg, aceita que doi menos..")

print("---------------------------------------------------------------")

print(f"velocidade inicial absoluta = {velocidadeinicial(forca, m):.2f}m/s")
print(f"velocidade horizontal inicial = {velocidadeinicialx(forca, m, angulo):.2f}m/s")
print(f"velocidade vertical inicial = {velocidadeinicialy(forca, m, angulo):.2f}m/s")

print("---------------------------------------------------------------")
print("---------------------------------------------------------------")

print("velocidades de voo ao longo da voo loko (lol):")

print("---------------------------------------------------------------")
print("---------------------------------------------------------------")


for i in range(10):
    j = i/10
    t = tempodevoo(forca, m, angulo) * j
    vx = velocidadex(forca, m, angulo, t)
    vy = velocidadey(forca, m, angulo, t)



    print(f"a velocidade no instante {t:.2f} foi:")
    print(f"\thorizontal: {vx:.2f} m/s")
    print(f"\tvertical: {vy:.2f} m/s")