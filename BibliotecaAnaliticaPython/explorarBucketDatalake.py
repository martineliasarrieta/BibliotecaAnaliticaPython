def explorarBucketDatalake(bucket_name):

    """
    Esta funcion permite explorar el contenido existente dentro de un bucket en el datalake
    Solo devuelve el contenido si el usuario tiene permisos de lectura sobre el bucket consultado
    
    Uso:
        explorarBucketDatalake('landing-zone-analitica')
    
    """
    
    import boto3
    
    client = boto3.client('s3')
    paginator = client.get_paginator('list_objects')
    result = paginator.paginate(Bucket=bucket_name, Delimiter='/')
    for prefix in result.search('CommonPrefixes'):
        print(prefix.get('Prefix'))

