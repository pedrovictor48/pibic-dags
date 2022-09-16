import requests
from cities.utils import postar

TOKEN = "d1bb804b2deb44121c369766969557fac53d34fa4b595f884c13f81ca6de5245" #felipe
URLAPI = "http://api.olhovivo.sptrans.com.br/v2.1"

def req() -> dict:
    auth = requests.post(url=(URLAPI + "/Login/Autenticar?token=" + TOKEN))
    if auth.text != 'true':
        raise "Houve um erro na autenticação"

    response = requests.get(URLAPI + "/Posicao", cookies=auth.cookies)
    response = response.json()

    return response;

def process_response(response: dict) -> list:
    lista_onibus = list()
    for linha in response['l']:
        for vs in linha['vs']:
            instancia_processada = {
                'latitude': vs['py'],
                'longitude': vs['px'],
                'tempo_captura': vs['ta'],
                'id_onibus': vs['p']
            }
            #enfim vamos adicionar a nova instância processada na lista
            lista_onibus.append(instancia_processada)
    
    return lista_onibus

def sao_paulo():
    response = req();
    processed_response = process_response(response)
    postar(process_response)