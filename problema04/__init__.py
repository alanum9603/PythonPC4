from package.bitcoin import get_BTC
from package.mngtxt  import wrt

def __init__() : 
    x = get_BTC()
    print(x)
    while True :
        q = input('¿Qué desea hacer? Solo digite el número\n1. Guardar actualización\n2. Actualizar información\n3. Salir\n -> ')
        match q :
            case '1' :
                print(wrt(x))
                x = get_BTC()
                print(f'\n{x}')
                continue
            case '2' :
                x = get_BTC()
                print(f'\n{x}')
                continue
            case '3' :
                break
            case _ :
                print('Error, debe digitar un valor dentro del menú\n')
                continue

if __name__ == '__main__' : 
    __init__()