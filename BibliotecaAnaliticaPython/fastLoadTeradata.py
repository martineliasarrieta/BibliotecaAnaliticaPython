def fastLoadTeradata(table_name, n_campos, createTable, df):
    
    """
        Funcion de carga rapida a teradata, solo es util cuando se van a cargar mas de 100 mil registros
        Antes de usarla se debe definir la estructura de la tabla (definicion de los campos) que se pasara 
        a la funcion por medio del parametro createTable, y ademas el data frame con los datos a insertar como df
        
        Uso:
            fastLoadTeradata("Base_Datos.Nombre_tabla", 84, createTable, df )
    """
    
    dropQry = "DROP TABLE " + table_name
    
    #Generacion de (?) para campos definición de campos vacios
    string = '?,'
    n = ('('+''.join([string] * n_campos)[:-1]+')')
        
    insertQry = "{fn teradata_sessions(20)}{fn teradata_require_fastload} insert into " + table_name + ' ' + n
    
    #Definición de null en el df
    rows = df.where((pd.notnull(df)), None).values.tolist()
    
    try:
        with con.cursor () as cur:
            cur.execute (dropQry)
            cur.execute (createTable)
            cur.execute (insertQry, rows)
            
    except:
        with con.cursor () as cur:
            cur.execute (createTable)
            cur.execute (insertQry, rows)
            
    