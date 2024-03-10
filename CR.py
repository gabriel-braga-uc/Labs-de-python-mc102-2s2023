# Listas separadas contendo, em ordem, nota e peso respectivamente de cada matéria.  
ma141_np = [10, 4]
ma111_np = [10, 6]
me110_np = [10, 4]
me111_np = [10, 3]
ms149_np = [10, 2]
me210_np = [10, 4]
ma211_np = [10, 6]
la142_np = [10, 4]
la118_np = [10, 4]
ma327_np = [10, 4]
mc102_np = [10, 6]

# União de todas essas listas em uma grande lista.  
materias_np = [ma141_np, ma111_np, me110_np, me111_np, ms149_np, me210_np, ma211_np, la142_np, la118_np, ma327_np, mc102_np]

peso_total = 0
dividendo_media = 0

for x in materias_np:
    peso_total += x[1]
    dividendo_media += (x[0] * x[1])

print(peso_total)
print(dividendo_media)

media_ponderada_final = dividendo_media / peso_total

print(media_ponderada_final)