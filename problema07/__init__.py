from database.connection import insertRows, listRows
from package.sunat import get_data_per_month
import time

def sw_month(i) :
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    return months[i]

def __init__() :
    try : 
        print('A continuación, se van a insertar los tipos de cambio de soles (PEN) a dolares (USD)')
        for i in range(12) :
            list = get_data_per_month(i+1)
            time.sleep(0.5)
            insertRows(list)
            print(f'Tipo de cambio de {sw_month(i)} añadido correctamente')
            time.sleep(0.5)
    except Exception as err :
        print(f'Error: {err}')
    print('Columnas añadidas correctamente')
    print('|Fecha        |Compra|Venta |')
    x = listRows()
    for row in x :
        print(row)

if __name__ == '__main__' :
    __init__()