def queryTeradata(myQuery, user, password):

    """
    Esta función permite hacer consultas tipo SQL a teradata mediante un query, 
    pasando como parametros el user y la contraseña
    establecidos para teradata
    
    Uso: 
        queryTeradata("SELECT * FROM XXXX",  "user", "password")
    """

    import teradatasql
    import pandas as pd
    
    con = teradatasql.connect(host='10.205.24.12', 
                          user=user, 
                          password = password )
    df = pd.read_sql(myQuery, con)
    return df