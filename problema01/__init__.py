from package.bitcoin import btc_to_val, get_ctrys

def __init__() : 
    while True :
        coin = input('Digite la moneda a la que desea hacer el cambio, digite 1 si desea ver las monedas disponibles -> ')
        if coin == '1' :
            print(get_ctrys())
            continue
        break
    while True :
        try :
            btc = float(input('Digite cuantos bitcoins tiene -> '))
            res = btc_to_val(btc, coin)
        except Exception as err :
            print(f'Error: {err}')
            continue
        else :
            print(f'\n{res}')
            break

if __name__ == '__main__' : 
    __init__()