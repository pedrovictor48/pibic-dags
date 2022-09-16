import requests
from cities.utils import postar

URLAPI = "https://jeap.rio.rj.gov.br/dadosAbertosAPI/v2/transporte/veiculos/onibus2"

def req() -> dict:
    response = requests.get(URLAPI).json()
    return response 

def process_response(response: dict) -> list:
    lista_onibus = list()
    for vs in response:
        instancia_processada = {
            'latitude' : vs['laitutde'],
            'longitude' : vs['longitude'],
            'tempo_captura' : vs['dataHora'],
            'id_onibus' : vs['ordem']
        }
        lista_onibus.append(instancia_processada)
    return lista_onibus


def rio():
    response = req();
    processed_response = process_response(response)
    postar(process_response)