def listarBucketsDatalake():
    
    """
    Esta función lista los buckets del datalake existentes en AWS S3. Devuelve una lista con los nombres.
    Se requiere un access_key_id y un aws_secret_key_id que son generados
    cuando se solicita el acceso al datalake, para ser establecidos a traves de aws CLI en el computador.
    
    Uso: listarBucketsDatalake()
    
    """
    
    import boto3
   
    client = boto3.client('s3')

    response = client.list_buckets()

            # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print (f'  {bucket["Name"]}')