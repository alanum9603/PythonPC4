import os
import zipfile

dir_unzip = '/workspaces/PythonPC4/problema03/src/unzip'
dir_zip = '/workspaces/PythonPC4/problema03/src/zip'

def validate_route_zip() :
    if not os.path.isdir(dir_zip): 
        os.mkdir(dir_zip) 

def validate_route_unzip() :
    if not os.path.isdir(dir_unzip): 
        os.mkdir(dir_unzip) 

# creando un archivo zipeado
def zip(route_arc) :
    validate_route_zip()

    try :
        files = os.listdir(route_arc)
    except :
        route_arc = '/workspaces/PythonPC4/problema03/src/img'
        files = os.listdir(route_arc)

    with zipfile.ZipFile('/workspaces/PythonPC4/problema03/src/zip/archivos.zip', 'w') as zip:
        for file in files:
            file_path = os.path.join(route_arc, file)

            if os.path.isfile(file_path):
                zip.write(file_path
                          ,  os.path.basename(file_path) # para evitar subcarpetas
                          )
                
def unzip(route_arc) :
    validate_route_unzip()

    if not os.path.isfile(route_arc) :
        route_arc = f'{dir_zip}/archivos.zip'

    # extración de archivos
    with zipfile.ZipFile(route_arc, 'r') as zip_ref:
        zip_ref.extractall(path=dir_unzip)
                
def __init__() :
    validate_route_zip()
    validate_route_unzip()

if __name__ == '__main__' :
    __init__()
