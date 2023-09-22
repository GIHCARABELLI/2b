vo = int(input('qual a velocidade inicial do lançamento obliquo?'))
a = int(input('o tempo total do voo?'))
t = int(input(' o local da queda?'))

v = vo + a*t
s = (0.5) * (a) * (t**2)
print('o valor da velocidade e do espaço valem {} m/s e {} metros'.format(v,s))


