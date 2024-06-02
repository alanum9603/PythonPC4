import requests

def get_data_sunat() :
    try :
        url = f'https://api.apis.net.pe/v1/tipo-cambio-sunat'
        response = requests.get(url)
        data = response.json()
        fecha = data['fecha']
        compra = data['compra']
        list = { 'updated' : fecha, 'compra' : compra}
    except Exception as err :
        print(f'Error: {err}')
    else : 
        return list

def __init__() :
    print(get_data_sunat())
    
if __name__ == '__main__' :
    __init__()