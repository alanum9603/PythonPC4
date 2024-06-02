import sqlite3 as sql
route_db = '/workspaces/PythonPC4/problema07/database/base.db'
name_tb =  'sunat_info'
def createDB() :
    try : 
        conn = sql.connect(route_db)
        conn.commit()
        conn.close()
    except Exception as err :
        conn.close()
        print(f'Error: {err}')

def createTable() :
    query = f'''
    CREATE TABLE {name_tb} (
        fecha DATE,
        compra FLOAT,
        venta FLOAT
    )
    '''
    try : 
        conn = sql.connect(route_db)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
    except Exception as err :
        conn.close()
        print(f'Error: {err}')

def insertRows(list) :
    try :
        query = f'INSERT INTO {name_tb} (fecha, compra, venta) VALUES (?, ?, ?)'
        conn = sql.connect(route_db)
        cursor = conn.cursor()
        cursor.executemany(query, list)
        conn.commit()
        conn.close()
    except Exception as err :
        conn.close()
        print(f'Error: {err}')
        
def listRows() :
    try : 
        query = f'SELECT * FROM {name_tb}'
        conn = sql.connect(route_db)
        cursor = conn.cursor()
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
    except Exception as err :
        conn.close()
        print(f'Error: {err}')
    else :
        return datos

def __init__() :
    createDB()
    createTable()
    pass

if __name__ == '__main__' :
    __init__()