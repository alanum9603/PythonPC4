import requests

def get_data_per_month(i) : 
    try :
        list = []
        url = f'https://api.apis.net.pe/v1/tipo-cambio-sunat?month={i}&year=2023'
        response = requests.get(url)
        data = response.json()
        for j in range (len(data)) :
            fecha = data[j]['fecha']
            compra = data[j]['compra']
            venta = data[j]['venta']
            list.append((fecha, compra, venta))
    except Exception as err :
        print(f'Error: {err}')
    return list

def __init__() :
    pass
    
if __name__ == '__main__' :
    __init__()