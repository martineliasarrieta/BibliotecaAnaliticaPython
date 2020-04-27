def cargarDatosDatalake(local_file, bucket_name, folder, s3_file_name):
    
    """

    Funcion que carga un archivo local a AWS S3
    local_file es la ruta del archivo a cargar, incluyendo el nombre de este
    bucket_name nombre del bucket en s3 donde se quiere cargar el archivo al datalake
    folder nombre de la carpeta contenida dentro del bucket que va a contener el archivo dentro del DL
    s3_file_name nombre con el que quiere que quede guardado dentro del datalake
    
    Uso: 
        cargarDatosDatalake('D:/Usuarios/xxxx', 
                    'landing-zone-xxxx', 
                    'folder_bucket','holamundo.csv')
        
    Desde Jupyter, para subir archivo en la misma ubicación del notebook
    de trabajo:
        cargarDatosDatalake('holamundo.csv', 
                'landing-zone-xxxx', 
                'folder_bucket','holamundojupyter.csv')
    """

    import boto3
    from botocore.exceptions import NoCredentialsError
    
    s3 = boto3.resource('s3')
    path = folder +'/'+ s3_file_name

    try:
        s3.meta.client.upload_file(local_file, bucket_name, path)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


