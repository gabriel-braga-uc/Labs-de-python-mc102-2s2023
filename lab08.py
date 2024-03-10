# Aluno: Gabriel Ozélo Braga; RA: 247345; Turma: D #
tamanho = int(input())
palavras = []
final = []
palavras_sorted = []

while tamanho > 0:
    tamanho -= 1
    palavras.append(input())
for x in palavras:
    palavras_sorted.append(''.join(sorted(x)))
count_x = 0

tamanho_2 = len(palavras_sorted)


palavras_sorted_unique = list(dict.fromkeys(palavras_sorted))
tamanho_2 = len(palavras_sorted_unique)
while tamanho_2 > 0:
    tamanho_2 -= 1
    final.append([])


for x in palavras:
    for y in palavras_sorted_unique:
        if ''.join(sorted(x)) == y:
            final[palavras_sorted_unique.index(y)].append(x)
            break

for x in final:
    print('-'.join(x))