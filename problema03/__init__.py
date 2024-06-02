from package.zipper import zip, unzip

def __init__() :
    dir_to_zip = input('Digite la ruta del directorio que quiere zipear, no digite nada para usar una ruta predeterminada\n -> ')
    zip(dir_to_zip)
    dir_to_unzip = input('Digite la ruta del archivo que quiere extraer, no digite nada para usar una ruta predeterminada\n -> ')
    unzip(dir_to_unzip)

if __name__ == '__main__' :
    __init__()