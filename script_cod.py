import datetime
import requests

def cod_inicial(data=datetime.date.today()):    
    dia = ("0" + str(data.day))[-2:]
    mes = ("0" + str(data.month))[-2:]
    codigo = int(dia+mes)*int(mes+dia)    
    codigo = "0" + str(codigo)
    codigoTratado = codigo[-6:]
    return codigoTratado
    
def cod_externo(data = datetime.date.today()):
    dia = ("0" + str(data.day))[-2:]
    mes = ("0" + str(data.month))[-2:]
    codigo = int(dia+dia)*int(mes+mes)
    codigo = "0" + str(codigo)
    codigoTratado = codigo[-6:]
    return codigoTratado

def future_cods():
    data = datetime.date.today()
    i = 1
    while data.year == 2017:
        while i < 5:
            print (cod_inicial(data))
            i = i + 1
        data += datetime.timedelta(days=1)
        i = 1

base_url = 'http://blink.devicelab.com.br'
login_url = base_url + '/signin'
headers = {'Content-Type', 'application/json;charset=utf-8'}

r = requests.post(login_url,)
