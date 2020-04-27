def explorarFolderBucketDatalake(bucket_name, folder):
    
    """

    Esta funcion permite explorar el contenido existente de una carpeta ubicada de un bucket en el datalake
    Solo devuelve el contenido si el usuario tiene permisos de lectura sobre el bucket consultado
    
    Uso:
        explorarFolderBucketDatalake("landing-zone-analitica", 'Capacitacion')
    
    """
    
    import boto3
    
    s3 = boto3.resource('s3')
    bucket  =  s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=folder):
        print('{0}:{1}'.format(bucket.name, obj.key))
        
