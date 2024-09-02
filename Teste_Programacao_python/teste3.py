import json

#Função para carregar os dados do arquivo JSON
def carregar_dados(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
    return dados['faturamento_diario']

#Função para calcular o menor e maior valor de faturamento
def calcular_menor_maior_faturamento(dados):
    valores = [item['faturamento'] for item in dados if item['faturamento'] > 0]
    menor = min(valores) if valores else 0
    maior = max(valores) if valores else 0
    return menor, maior

#Função para calcular a media mensal
def calcular_media_mensal(dados):
    valores = [item['faturamento'] for item in dados if item['faturamento'] > 0]
    media = sum(valores) / len(valores) if valores else 0
    return media

#Função para contar os dias com faturamento superior à média
def contar_dias_acima_da_media(dados, media):
    contagem = sum(1 for item in dados if item['faturamento'] > media)
    return contagem

#Carrega o arquivo .json criado
arquivo = 'faturamento.json'
dados = carregar_dados(arquivo)

#Chamar as funções e printar os valores
menor, maior = calcular_menor_maior_faturamento(dados)
media = calcular_media_mensal(dados)
dias_acima_media = contar_dias_acima_da_media(dados, media)

print(f"Menor valor de faturamento: R${menor}")
print(f"Maior valor de faturamento: R${maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")