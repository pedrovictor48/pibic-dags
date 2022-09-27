import requests
from cities.utils import postar

URL = 'https://transporteservico.urbs.curitiba.pr.gov.br/getVeiculos.php?&c=e5b1c'

def req() -> dict:
    response = requests.get(URLAPI)
    response = response.json()

    return response;

def process_response(response: dict) -> list:
    lista_onibus = list()
    for cod in response:
        lista_onibus.append(response[cod])
    
    return lista_onibus

def curitiba():
    response = req();
    response_list = process_response(response)
    postar(response_list)
