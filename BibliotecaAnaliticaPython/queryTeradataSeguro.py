def queryTeradataSeguro(myQuery, user):

    import teradatasql
    import pandas as pd
    import os

    """
    Esta función permite hacer consulta SQL a teradata mediante un query, usando el password ecriptado en 
    dos archivos de llaves generados previamente mediante TJEncryptPassword.R
    las llaves que contienen la clave encriptada deben estar en el mismo directorio que el notebook a ejecutar
    
    Uso:
        queryTeradataSeguro("SELECT * FROM XXXX",  "usuario")
    """
    PASS_PATH = os.getenv('HOME')
    PASS_PATH += "/notebooks"
    con = teradatasql.connect(host='10.205.24.12', 
                          user=user, 
                          password = f"ENCRYPTED_PASSWORD(file:{PASS_PATH}/PassKey.properties,file:{PASS_PATH}/EncPass.properties)")
    df = pd.read_sql(myQuery, con)
    return df