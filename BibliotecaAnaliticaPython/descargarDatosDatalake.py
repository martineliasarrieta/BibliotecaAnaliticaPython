def descargarDatosDatalake(bucket_name, folder, s3_file_name, output_name):

    """
    
    Funcion que descarga archivos de aws S3 a un repositorio local
    
    Uso:
        
    Descargar en el directorio local del Notebook de jupyter
        descargarDatosDatalake('landing-zone-analitica', 
                    'xxxx-analitica', 
                    'holamundojupyter.csv', 
                    'holamundojupyter.csv')
        
    Descargar en directorio local del PC    
        descargarDatosDatalake('landing-zone-analitica', 
                    'xxxx-analitica', 
                    'holamundojupyter.csv', 
                    'D:/Usuarios/xxxx/Desktop/holamundojupyter.csv')
    """

    import boto3
    from botocore.exceptions import NoCredentialsError
    
    s3 = boto3.resource('s3')
    path = folder +'/'+ s3_file_name
    try:
        s3.meta.client.download_file(bucket_name, path, output_name) 
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False