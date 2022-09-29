import requests
from cities.utils import postar

CSV_LINK = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/flujo-vehicular-anillo-digital/dataset_flujo_vehicular.csv'

def process_response(dados):
    linhas = dados.split('\n')
    linhas = linhas[1:-1]
    
    veiculos = []
    for linha in linhas:
        valores = linha.split(',')
        veiculo = dict()

        veiculo['latitude'] = valores[4]
        veiculo['longitude'] = valores[5]
        veiculo['hora'] = valores[1]
        veiculo['id_onibus'] = valores[0]

        veiculos.append(veiculo)
    
    return veiculos

def buenos_aires():
    csv_req = requests.get(CSV_LINK)
    dados = csv_req.content.decode('utf-8-sig')
    processed_response = process_response(dados)
    postar(processed_response)
