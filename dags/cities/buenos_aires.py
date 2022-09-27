import requests
from cities.utils import postar

CSV_LINK = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/flujo-vehicular-anillo-digital/dataset_flujo_vehicular.csv'

def dictfy(linha, atributos):
    dictfied = dict()
    for idx, coluna in enumerate(linha.split(',')):
        dictfied[atributos[idx]] = coluna
    
    return dictfied

def req() -> list:
    lista_onibus = list()
  
    csv_req = requests.get(CSV_LINK)
    dados = csv_req.content.decode('utf-8-sig')
    linhas = dados.split('\n')
    atributos = linhas[0].split(',')
    linhas = linhas[1:-1]

    for linha in linhas:
        json_doc = dictfy(linha, atributos)
        lista_onibus.append(json_doc)
        
    return lista_onibus;

def buenos_aires():
    response_list = req();
    postar(response_list)
