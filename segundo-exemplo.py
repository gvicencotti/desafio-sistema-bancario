import requests
import time

#criar um decorator calcular_tempo

def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(tempo_final - tempo_inicial)

    return wrapper


@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()