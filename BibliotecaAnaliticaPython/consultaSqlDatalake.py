def consultaSqlDatalake(workgroup, bucket_name, path, database, query):
    """

    Función que realiza una consutla SQL a AWS athena, devuelve en 
    dataframe una tabla.
    
    workgroup especificar el grupo de trabajo asignado a cada area de negocio
    
    uso: 
    consultaSqlDatalake('Group-Analitica', 
                'landing-zone-analitica', 
                'temp/athena/output',
                'dbtest01', 
                'SELECT * 
                FROM "dbtest01"."test01"'
                )    
    """

    import boto3
    import pandas as pd
    import io
    import re
    import time
    
    client_athena = boto3.client('athena')
    client_s3     = boto3.client('s3')
    
    response = client_athena.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': database
            },
            ResultConfiguration={
                'OutputLocation': 's3://' + bucket_name + '/' + path
            },
            WorkGroup= workgroup
        )
    
    execution = response
    execution_id = execution['QueryExecutionId']
    state = 'RUNNING'
    max_execution = 5
    while (max_execution > 0 and state in ['RUNNING']):
        
        max_execution = max_execution - 1
        response2 = client_athena.get_query_execution(QueryExecutionId = execution_id)
    
        if 'QueryExecution' in response2 and \
                'Status' in response2['QueryExecution'] and \
                'State' in response2['QueryExecution']['Status']:
            state = response2['QueryExecution']['Status']['State']
            if state == 'FAILED':
                return False
            elif state == 'SUCCEEDED':
                s3_path = response2['QueryExecution']['ResultConfiguration']['OutputLocation']
                filename = re.findall('.*\/(.*)', s3_path)[0]
                #return filename
                s3_filename = filename
        time.sleep(1)
    s3_filename = filename        
            
    
    obj = client_s3.get_object(Bucket=bucket_name,
                              Key=path + '/' + s3_filename
                                )
    
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))  
    
    print('La consulta se guardo en s3://'+bucket_name+'/'+path, ' nombrado con el codigo ', s3_filename)
    
    return df
   
   