# Aluno: Gabriel Ozélo Braga; RA: 247345; Turma: D

T = int(input())
L1 = int(input())
L2 = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())
valor_passagem = 6

# Gasto caso 1:
gasto_c1 = L1 + valor_passagem * 2

# Gasto caso 2:
gasto_c2 = L2 + valor_passagem 

# Tempo gasto caso 1 (minutos):
tempo_gasto_c1 = P1 + T + P2

# Tempo gasto caso 2 (minutos):
tempo_gasto_c2 = T + P3

#print("Caso 1: " + str(tempo_gasto_c1) + " min, R$" + str(gasto_c1), "\nCaso 2: " + str(tempo_gasto_c2) + " min, R$" + str(gasto_c2))

gasto_c1 = int(gasto_c1)
gasto_c2 = int(gasto_c2)
tempo_gasto_c1 = int(tempo_gasto_c1)
tempo_gasto_c2 = int(tempo_gasto_c2)


if tempo_gasto_c1 > 45 and tempo_gasto_c2 > 45:
    if tempo_gasto_c1 == tempo_gasto_c2:
        print(True)
    elif tempo_gasto_c1 < tempo_gasto_c2:
        print(True)
    else:
        print(False)
elif tempo_gasto_c1 <= 45 and tempo_gasto_c2 <= 45:
    if gasto_c1 == gasto_c2:
        print(True)
    if gasto_c1 < gasto_c2:
        print(True)
    elif gasto_c2 < gasto_c1:
        print(False)
elif tempo_gasto_c1 < tempo_gasto_c2:
    print(True)
else:
    print(False)
        