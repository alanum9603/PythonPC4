from package.readpy import count_lines_py
def __init__() : 
    route = input('Digite la ruta del archivo .py que desea revisar\n -> ')
    res = count_lines_py(route)
    print(res)

if __name__ == '__main__' :
    __init__()