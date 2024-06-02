from package.mngtxt import write_table, search_table, search_line_in_table

def getn_min_max(min, max) :
    while True : 
        try : 
            x = int(input(f'Digite un número entero entre {min} y {max} -> '))
            if x < min or x > max :
                print(f'El número debe estar entre {min} y {max}')
                continue
        except : 
            print('Error, debe digitar un número entero')
            continue
        else :
            break
    return x
    

def __init__() : 
    while True :
        print('¿Que desea hacer?\n1. Generar tabla de multiplicar de un número n\n2. Buscar tabla en archivo txt\n3. Buscar línea específica de una tabla de multiplicar en un archivo txt\n4. Salir')
        q = getn_min_max(1, 4)
        match q : 
            case 1 :
                print('Seleccionó Generar tabla de multiplicar y guardar en archivo txt')
                x = getn_min_max(1, 10)
                print(write_table(x))
            case 2 : 
                print('Seleccionó Buscar tabla de multiplicar en archivo txt')
                x = getn_min_max(1, 10)
                print(search_table(x))
                pass
            case 3 :
                print('Seleccionó Buscar línea específica de tabla de multiplicar en archivo txt\nQue tablade multiplicar desea buscar?')
                x = getn_min_max(1, 10)
                print('¿Que línea desea recuperar?')
                y = getn_min_max(0, 10)
                print(search_line_in_table(x, y))
                pass
            case 4 : 
                break
if __name__ == '__main__' :
    __init__()