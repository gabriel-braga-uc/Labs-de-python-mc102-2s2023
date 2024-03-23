# Listas separadas contendo, em ordem, nota e peso respectivamente de cada matéria.  
np1 = [1, 4]
np2 = [2, 6]
np3 = [3, 4]
np4 = [4, 3]
np5 = [5, 2]
np6 = [6, 4]
np7 = [7, 6]
np8 = [8, 4]
np9 = [9, 4]
# União de todas essas listas em uma grande lista.  
materias_np = [np1, np2, np3, np4, np5, np6, np7, np8, np9]

peso_total = 0
dividendo_media = 0

for x in materias_np:
    peso_total += x[1]
    dividendo_media += (x[0] * x[1])

print(peso_total)
print(dividendo_media)

media_ponderada_final = dividendo_media / peso_total

print(media_ponderada_final)