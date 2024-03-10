# Aluno: Gabriel Ozélo Braga; RA: 247345; Turma: D #

tamanho = int(input())
tamanho_count = tamanho
serie = []

while tamanho_count != 0:
    tamanho_count -= 1
    serie.append(int(input()))

limiar = int(input())

differencas_absolutas = []
differencas_absolutas_temp = []
for x in serie:
    for y in serie:
        w = x - y
        if w < 0:
            w *= -1
        differencas_absolutas_temp.append(w)
    differencas_absolutas.append(differencas_absolutas_temp)
    differencas_absolutas_temp = []

binary_indicator = []
binary_indicator_temp = []
for x in differencas_absolutas:
    for y in x:
        if y <= limiar:
            binary_indicator_temp.append(0)
        else:
            binary_indicator_temp.append(1)
    binary_indicator.append(binary_indicator_temp)
    binary_indicator_temp = []

count = 0
for x in binary_indicator:
    for y in x:
        count += 1
        if count != tamanho:
            print(str(y) + ' ', end='')
        else:
            print(str(y), end='')
    count = 0
    print()