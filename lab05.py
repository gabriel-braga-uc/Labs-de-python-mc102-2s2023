

roleta_partes, valor_viagem, premio = input().split()
roleta_partes = int(roleta_partes)
valor_viagem = int(valor_viagem)
premio = float(premio)
prob_viagem = 0
premio_medio = 0

partes = roleta_partes
fatias = []

# Leitura da roleta

while partes != 0:
    parte = str(input())
    parte_dividida = parte.split(' ')
    parte_operacao = parte_dividida[0]
    parte_valor = parte_dividida[1]
    parte_tipo = parte_dividida[2]

    if parte_tipo == 'Reais':
        valor = float(str(parte_operacao) + str(parte_valor))

        if valor * -1 > premio:
            valor = 0
            fatias.append([valor, 0])
        else:
            fatias.append([valor, (premio + valor)])

    elif parte_tipo == '%':
        valor = (premio * float(str(parte_operacao) + str(parte_valor))) / 100

        if valor * -1 > premio:
            valor = 0
            fatias.append([valor, 0])
        else:
            fatias.append([valor, (premio + valor)])

    partes -= 1

# Calculo da probabilidade

premios = []

for fatia in fatias:
    premios.append(fatia[1])

premio_medio = sum(premios) / len(fatias)

possibilidades = 0

for fatia in fatias:
    is_positive = bool(fatia[0] + premio >= valor_viagem)

    if is_positive:
        possibilidades += 1

prob_viagem = (possibilidades / len(fatias)) * 100

# Imprime a probabilidade do premio final ser suficiente para a viagem
print("{:.2f}%".format(prob_viagem))
# Imprime o valor médio do premio final a ser recebido
print("R$ {:.2f}".format(premio_medio))