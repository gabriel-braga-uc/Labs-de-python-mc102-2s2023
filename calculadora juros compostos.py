capital = 100000 #Dinheiro incial#

juros_anual = 0.38 #Valor do juros ao ano##
intervalo_dias = 20 #De quanto em quanto tempo é aplicado o juros em dias#

aporte_mediano_diario = 30 #Aporte médio por dia#
intervalo_aporte = 2500  #De quanto em quanto tempo é depositado um aporte#

tempo_dias = 365*15 + (365/12)*0 + 0 #Quanto tempo dura o investimento em dias#




cu = tempo_dias
contagem_aporte = intervalo_aporte - 1
contagem_intervalo = intervalo_dias - 1
dia = 0
aporte_acumulado = 0
inicial = capital
aporte_acumulado_total = 0
while tempo_dias > 0:
    dia += 1
    if contagem_intervalo == 0:
        juros_acumulado = (juros_anual/365)*intervalo_dias
        capital += capital*(juros_acumulado)
        contagem_intervalo = intervalo_dias - 1
        print('Saldo no dia ' + str(dia) + ": " + str(capital))
    else:
        contagem_intervalo -= 1
        
    if aporte_mediano_diario > 0:
        if contagem_aporte == 0:
            aporte_acumulado = aporte_mediano_diario*intervalo_aporte
            aporte_acumulado_total += aporte_acumulado
            capital += aporte_acumulado
            contagem_aporte = intervalo_aporte - 1
        else:
            contagem_aporte -= 1
    tempo_dias -= 1
    
    
diferenca = capital - ((((juros_anual/365)*cu)*inicial)+inicial + aporte_acumulado_total)
print("Diferença pro juros normal: " + str(round(diferenca)))
print("Capital final menos aporte total: " + str(round(capital)) + "-" + str(round(aporte_acumulado_total)) + ': ' + str(round(capital-aporte_acumulado_total)))
print("Rendimento anual aplicado ao capital final: ", str((juros_anual)*capital))