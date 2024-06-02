import os

dir_src = '/workspaces/PythonPC4/problema04/src'
dir_txt = '/workspaces/PythonPC4/problema04/src/updates_bitcoin.txt'

def validate_route() :
    if not os.path.isdir(dir_src): 
        os.mkdir(dir_src) 

def wrt(upd):
    validate_route()
    try: 
        with open(dir_txt,'a') as f:
            f.write(f'{upd}\n')
    except Exception as err :
        return f'Error: {err}'
    else :
        return 'Información agregada correctamente'

def __init__() :
    validate_route()

if __name__ == '__main__' :
    __init__()