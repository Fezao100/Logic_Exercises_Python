#Função que calcua o percentual de participação por estado
def percentual_particip_total(estado):
    fatura_sp = 67836.43
    fatura_rj = 36678.66
    fatura_mg = 29229.88
    fatura_es = 27165.48
    fatura_outros = 19849.53
    total_fatura = fatura_sp + fatura_rj + fatura_mg + fatura_es + fatura_outros

    if estado == 'sp' or estado == 'SP':
        percentual = (fatura_sp*100)/total_fatura
        return print(f"O percentual de SP na fatura total foi de: {percentual:.3f}%")
    elif estado == 'rj' or estado == 'RJ':
        percentual = (fatura_rj*100)/total_fatura
        return print(f"O percentual do RJ na fatura total foi de: {percentual:.3f}%")
    elif estado == 'mg' or estado == 'MG':
        percentual = (fatura_mg*100)/total_fatura
        return print(f"O percentual de MG na fatura total foi de: {percentual:.3f}%")
    elif estado == 'es' or estado == 'ES':
        percentual = (fatura_es*100)/total_fatura
        return print(f"O percentual de ES na fatura total foi de: {percentual:.3f}%")
    else:
        percentual = (fatura_outros*100)/total_fatura
        return print(f"O percentual dos outros estados na fatura total foi de: {percentual:.3f}%")

continua = 1

#Loop para verificar o percentua de cada estado
while continua != 0:
    estado = str(input("\nDeseja ver o percentual de faturamento de qual estado (UTILIZAR A SIGLA)? ")) 
    percentual_particip_total(estado)

    continua = input("\nSe dejesa ver o percentual de outro estado digite qualquer número, para sair digite 0: ")