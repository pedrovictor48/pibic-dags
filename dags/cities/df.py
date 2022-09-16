import requests
from cities.utils import postar

URLAPI = "https://www.sistemas.dftrans.df.gov.br/service/gps/operacoes"

def req():
    response = requests.get(URLAPI).json()
    return response

def process_response(response: dict) -> list:
    lista_onibus = list()
    for operadora in response:
        for vs in operadora['veiculos']:
            instancia_processada = {
                'latitude': vs['localização']['longitude'],
                'longitude': vs['localização']['latitude'],
                'tempo_captura': vs['horario'],
                'id_onibus': vs['numero']
            }
            lista_onibus.append(instancia_processada)
    return lista_onibus

def df():
    response = req();
    processed_response = process_response(response)
    postar(process_response)