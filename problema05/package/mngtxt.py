import os

dir_src = '/workspaces/PythonPC4/problema05/src'
dir_txt = '/tabla-n.txt'

def validate_route() :
    if not os.path.isdir(dir_src): 
        os.mkdir(dir_src) 

def create_mult_table(n) :
    res = f'Tabla del {n}\n'
    for i in range (10) :
        res += f'{(i+1):02} x {n} = {((i+1) * n):02}\n'
    return res

def write_table(n):
    validate_route()
    table = create_mult_table(n)
    try: 
        with open(f'{dir_src}{dir_txt}','a') as f:
            f.write(f'{table}\n')
    except Exception as err :
        return f'Error: {err}'
    else :
        return 'Información agregada correctamente'

def search_table(n) : 
    text = f'Tabla del {n}\n'
    res = ''
    cont = 0
    try :
        with open(f'{dir_src}{dir_txt}','r') as f :
            for l in f.readlines() :
                if l == text or (cont < 11 and cont > 0) :
                    res += l
                    cont += 1
                elif cont == 11 : 
                    break
        if res == '' :
            res += 'Tabla no encontrada'
    except FileNotFoundError :
        res += 'Archivo tabla-n.txt no encontrado'
    except Exception as err :
        res += f'Error: {err}'
    return res

def search_line_in_table(x, y) :
    try : 
        table = search_table(x).split('\n')
        print(table[y])
    except :
        return search_table(x)

def __init__() :
    validate_route()
    search_line_in_table(5, 3)

if __name__ == '__main__' :
    __init__()