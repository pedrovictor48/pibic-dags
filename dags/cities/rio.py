import requests
from cities.utils import postar

URLAPI = "https://jeap.rio.rj.gov.br/dadosAbertosAPI/v2/transporte/veiculos/onibus2"

def req() -> dict:
    response = requests.get(URLAPI).json()
    return response 

def process_response(response: dict) -> list:
    lista_onibus = list()
    for vs in response:
        lista_onibus.append(vs)
        
    return lista_onibus


def rio():
    response = req();
    response_list = process_response(response)
    postar(response_list)
