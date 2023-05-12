from bs4 import BeautifulSoup
from datetime import datetime
from db import *
import requests


inicio_url = 'http://'
ips_impressoras = ['10.151.33.51', '10.151.30.11', '10.151.30.5', '10.151.30.24',
                   '10.151.30.15', '10.151.30.42', '10.151.30.12', '10.151.33.86'
                   ]
url_contador = '/web/guest/br/websys/status/getUnificationCounter.cgi'

data_hora = datetime.now()
data_formatada = data_hora.strftime("%d/%m/%Y %H:%M:%S")


def manda_db(contador, ip):
    """Essa função vai separar os dados obtidos e enviar paras os respectivos bancos de dados"""
    if ip == ips_impressoras[0]:
        session.add(Clinica(data=data_formatada, contador=int(contador)))
        session.commit()
    elif ip == ips_impressoras[1]:
        session.add(Psicologia(data=data_formatada, contador=int(contador)))
        session.commit()
    elif ip == ips_impressoras[2]:
        session.add(Cordenacao(data=data_formatada, contador=int(contador)))
        session.commit()
    elif ip == ips_impressoras[3]:
        session.add(ApoioMulti(data=data_formatada, contador=int(contador)))
        session.commit()
    elif ip == ips_impressoras[4]:
        session.add(Biblioteca(data=data_formatada, contador=int(contador)))
        session.commit()
    elif ip == ips_impressoras[5]:
        session.add(Secretaria(data=data_formatada, contador=int(contador)))
        session.commit()
    elif ip == ips_impressoras[6]:
        session.add(SecAcad(data=data_formatada, contador=int(contador)))
        session.commit()
    elif ip == ips_impressoras[7]:
        session.add(Comercial(data=data_formatada, contador=int(contador)))
        session.commit()


def pega_contador(url_personalizada, ip):
    """Essa função vai fazer o scrape da contagem de impressoes"""
    try:
        pagina = requests.get(url_personalizada)
        soup = BeautifulSoup(pagina.content, "html.parser")
        tabela_contador = soup.find_all('table')[10]
        celula_contador = tabela_contador.find_all('td')[3]
        manda_db(celula_contador.text, ip)
    except:
        print('Deu Ruim meu chapa!')


# Esse loop vai automatizar a mudança de links e chamar a função pega_contador
for ip in ips_impressoras:
    url = inicio_url + ip + url_contador
    pega_contador(url, ip)
