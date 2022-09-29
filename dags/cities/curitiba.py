import requests
from cities.utils import postar

URL = 'https://transporteservico.urbs.curitiba.pr.gov.br/getVeiculos.php?&c=e5b1c'

def req():
    response = requests.get(URL).json()
    return response
    
def process_response(response):
    veiculos = []

    tabela_de_veiculos = {
        '':'NAO ESPECIFICADO',
        '1':'COMUM',
        '2':'SEMI PADRON',
        '3':'PADRON',
        '4':'ARTICULADO',
        '5':'BIARTICULADO',
        '6':'MICRO',
        '7':'MICRO ESPECIAL',
        '8':'BIARTIC. BIO',
        '9':'ARTIC. BIO',
        '10':'HIBRIDO',
        '11':'HIBRIDO BIO',
        '12':'ELÉTRICO}',
    } 

    for cod in response:
        veiculo = dict()

        veiculo['id_onibus'] = cod
        veiculo['latitude'] = response[cod]['LAT']
        veiculo['longitude'] = response[cod]['LON']
        veiculo['tempo_captura'] = response[cod]['REFRESH'] # <-- DEVE SER AJUSTADO!!! NAO VEM COM A DATA!!!
        veiculo['tipo_veiculo'] = tabela_de_veiculos[response[cod]['TIPO_VEIC']]

        veiculos.append(veiculo)

    return veiculos

def curitiba():
    response = req()
    processed_response = process_response(response)
    postar(processed_response)
