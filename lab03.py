
montante = input()
dias = input()
j_p = input()
j_t = input()

montante = float(montante)
dias = float(dias)
j_t = float(j_t)/100
j_p = float(j_p)/100

montante_p = j_p*montante

if dias <= 180:
    taxa = 0.225
elif dias > 180 and dias <= 360:
    taxa = 0.2
elif dias > 360 and dias <= 720:
    taxa = 0.175
elif dias > 720:
    taxa = 0.15

final_p = montante_p

final_t = (montante - ((montante + montante*j_t) - (((montante*j_t))*taxa)))*-1

print("Rendimento poupança: " + str("%0.2f" % round(final_p, 2)))
print("Rendimento tesouro: " + str("%0.2f" % round(final_t, 2)))

if (final_p > final_t):
    print("Maior rendimento: poupança")
else:
    print("Maior rendimento: tesouro")