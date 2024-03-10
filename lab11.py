###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11
# Nome: Gabriel Ozélo Braga
# RA: 247345
###################################################

tamanho = 15
mapa = []
mapa_matrix = []
while tamanho > 0:
    mapa.append('x x x x x x x x x x x x x x x')
    tamanho -= 1

ruas_x = (input()).split(' ')
ruas_y = (input()).split(' ')

for x in ruas_x:
    if int(x) == 0:
        mapa[0] = '. . . . . . . . . . . . . . .'

count_hor = 0
count_ver = 0

for a in mapa:
    count_hor += 1
    for x in ruas_x:
        if int(x) == count_hor:
            mapa[count_hor] = '. . . . . . . . . . . . . . .'
for a in mapa:
  temp_h = []
  for c in a:
    if c != ' ':
      temp_h.append(c)
  mapa_matrix.append(temp_h)
for x in mapa_matrix:
  for y in ruas_y:
    x[int(y)] = '.'

compradores = int(input())
n = 0
while compradores > 0:
    n += 1
    lote = (input()).split(' ')
    asdaffgfgfd = 0
    sup_es = []
    inf_dir = []
    while asdaffgfgfd < 2:
        sup_es.append(lote[asdaffgfgfd])
        asdaffgfgfd += 1
    while asdaffgfgfd < 4:
        inf_dir.append(lote[asdaffgfgfd])
        asdaffgfgfd += 1
    compradores -= 1
    py = -1
    hunt = False
    for linha in mapa_matrix:
        py += 1
        px = -1
        for p in linha:
            px += 1
            if (int(sup_es[0]) <= py <= int(inf_dir[0])) and (int(sup_es[1]) <= px <= int(inf_dir[1])):
                if p == 'x':
                    (mapa_matrix[py])[int(px)] = n
                else:
                    hunt = True
                    break
    if hunt:
        py2 = -1
        for x in mapa_matrix:
            py2 += 1
            px2 = -1
            for y in x:
                px2 += 1
                if str(y) == str(n):
                    (mapa_matrix[py2])[px2] = 'x'


for x in mapa_matrix:
    count = 0
    count2 = 0
    for y in x:
        count += 1
        if count < 15:
            print(str(y) + ' ', end = '')
        if (count == 15) and (count2 != 14):
            count2 += 1
            print(y)
        elif count2 == 14:
            print(y, end = '')