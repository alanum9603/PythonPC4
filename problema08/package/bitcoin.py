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
    

def get_data_BTC() :
    try:
        data = get_data()
        upd = data['time']['updatedISO']
        res = { 'updated' : upd }
        for bpi in data['bpi'] :
            code = data['bpi'][bpi]['code']
            valr = data['bpi'][bpi]['rate_float']
            res[f'{code}'] = valr
        return res
    except Exception as err :
        return f'Error: {err}'

def __init__() :
    get_data_BTC()
    
if __name__ == '__main__' :
    __init__()