
N = float(input())
N2 = N
notas = []
pesos = []
media_ponderada = 0.00
while N > 0:
    notas.append(float(input()))
    N -= 1
while N2 > 0:
    pesos.append(float(input()))
    N2 -= 1
#print(pesos)
count = 0
div = 0.00

for x in pesos:
    div += x
for x in notas:
    media_ponderada += x*pesos[count]
    count += 1
media_ponderada = media_ponderada/div

if media_ponderada >= 5:
    print("Media laboratorios:", format(media_ponderada, ".1f").replace(".", ","))
    print("Situacao: Aprovado por nota")
    print("Nota final:", format(media_ponderada, ".1f").replace(".", ","))
else:
    lab_exames = []
    try:
        M = float(input())
        continuar = True
    except:
        continuar = False
    if continuar:
        M2 = M
        notas_exame = []
        div2 =0
        while M > 0:
            lab_exames.append(int(input()))
            M -= 1
        for x in lab_exames:
            nota_exame = float(input())
            #print(x, lab_exames)
            peso_exame = pesos[x-1]
            div2 += pesos[x-1]
            notas_exame.append(nota_exame*peso_exame)
        WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=0
        for x in notas_exame:
            WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA += x

        notafinalexame = WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/div2
        if (notafinalexame+media_ponderada)/2 >= 5:
            print("Media laboratorios:", format(media_ponderada, ".1f").replace(".", ","))
            print("Situacao: Aprovado no exame")
            print("Nota final: 5,0")
        else:
            wawa = (notafinalexame+media_ponderada)/2
            print("Media laboratorios:", format(media_ponderada, ".1f").replace(".", ","))
            print("Situacao: Reprovado no exame")
            print("Nota final:", format(wawa, ".1f").replace(".", ","))
    else:
        print("Media laboratorios:", format(media_ponderada, ".1f").replace(".", ","))
        print("Situacao: Reprovado por nota")
        print("Nota final:", format(media_ponderada, ".1f").replace(".", ","))