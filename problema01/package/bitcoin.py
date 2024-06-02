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
    
def get_ctrys() :
    data = get_data()
    res = ''
    for i in data['bpi'] :
        code = data['bpi'][i]['code']
        ctry = data['bpi'][i]['description']
        res += f'{code} - {ctry}\n'
    return res

def get_values(bpi) :
    res = ''
    data = get_data()
    try:
        if not bpi in data['bpi'] :
            res += f'Error: Moneda no reconocida. Se utilizará la moneda predeterminada "USD"\n'
            bpi = 'USD'
        upd = data['time']['updated']
        code = data['bpi'][bpi]['code']
        ctry = data['bpi'][bpi]['description']
        symb = html.unescape(data['bpi'][bpi]['symbol'])
        valr = data['bpi'][bpi]['rate_float']
        res += f'Fecha: {upd}\nMoneda: {code} - {ctry} ({symb})'
    except TypeError:
        res += data
        valr = 0
    except Exception as err :
        res += f'Error: {err}'
        valr = 0
    return res, valr

def btc_to_val(btc : float, coin) :
    try :
        coin = coin.replace(' ','').upper()
        res, val = get_values(coin)
        btctoval = round(btc * val, 2)
    except : 
        res = get_values(coin)
        return res
    else :
        return f'{res}\nBitcoins: {btc}\nConversión a moneda: {btctoval}\n'
    
def __init__() :
    get_values('USD')
    
if __name__ == '__main__' :
    __init__()