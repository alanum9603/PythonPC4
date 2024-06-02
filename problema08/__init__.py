from package.bitcoin import get_data_BTC
from package.sunat   import get_data_sunat
from database.connection import insertRows, listRows, getLastRow

def __init__() : 
    try :
        BTC = get_data_BTC()
        sunat = get_data_sunat()
        fecha = BTC['updated']
        USD = BTC['USD']
        GBP = BTC['GBP']
        EUR = BTC['EUR']
        PEN = sunat['compra'] * BTC['USD']
        list_BTC = [fecha, USD, GBP, EUR, PEN]
        insertRows(list_BTC)
    except Exception as err :
        print(f'Error: {err}')
    while True :
        try :
            list = getLastRow()
        except Exception as err :
            print(f'Error: {err}')
        else :
            break
    while True :
        try :
            x = float(input('¿Cuantos bitcoins tiene? -> '))
        except Exception as err :
            print(f'Error: {err}') 
        else: 
            break
    print(f'''
Actualización: {list[0][0]}
BTC a USD : {round(list[0][1] * x, 2)}
BTC a GBP : {round(list[0][2] * x, 2)}
BTC a EUR : {round(list[0][3] * x, 2)}
BTC a PEN : {round(list[0][4] * x, 2)}
''')
    pass

if __name__ == '__main__' : 
    __init__()