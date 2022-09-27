import requests
from cities.utils import postar

URLAPI = "https://www.sistemas.dftrans.df.gov.br/service/gps/operacoes"

def req():
    response = requests.get(URLAPI).json()
    return response

def process_response(response: dict) -> list:
    lista_onibus = list()
    for item in response:
        lista_onibus.append(item)
                            
    return lista_onibus

def df():
    response = req();
    response_list = process_response(response)
    postar(response_list)
