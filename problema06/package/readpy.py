import os

def validate_code_line(txt : str) : 
    res = True
    line = txt.strip()
    if len(line) > 1 :
        if line[0] == '#' or line[0:3] == '"""' or line[0:3] == "'''" :
            res = False
    elif line == '' :
        res = False
    return res


def count_lines_py(r) : 
    try : 
        cont = 0
        with open(r, 'r') as f : 
            format = os.path.splitext(r)
            if format[1] != '.py' :
                return 'Error: Debe ser un archivo de formato .py'
            text = f.readlines()
            for line in text :
                x = validate_code_line(line)
                if x == True : 
                    cont += 1 
    except FileNotFoundError :
        return 'Error: Archivo no encontrado' 
    except Exception as err :
        return f'Error: {err}'
    else :
        return f'Número de líneas: {cont}'

def __init__() : 
    pass

if __name__ == '__main__' :
    __init__()