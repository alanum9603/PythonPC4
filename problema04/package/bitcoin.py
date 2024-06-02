import requests
import html

def get_data() :
    try :
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        data = response.json()
    except Exception as err : 
        return f'Error: {err}'
    else :
        return data
    
def format_data() :
    res = ''
    data = get_data()
    try:
        time = data['time']['updated']
        res += f'Actualización: {time}\n'
        for bpi in data['bpi'] :
            code = data['bpi'][bpi]['code']
            ctry = data['bpi'][bpi]['description']
            symb = html.unescape(data['bpi'][bpi]['symbol'])
            valr = data['bpi'][bpi]['rate_float']
            res += f'Moneda: {code} - ({symb}) {ctry}\n - Cambio: {valr}\n'
    except TypeError:
        res += data
    except Exception as err :
        res += f'Error: {err}'
    return res

def get_BTC() :
    res = format_data()
    return res
    
def __init__() :
    format_data()
    
if __name__ == '__main__' :
    __init__()