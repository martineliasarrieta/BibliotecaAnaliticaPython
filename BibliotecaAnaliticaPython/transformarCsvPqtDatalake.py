def transformarCsvPqtDatalake(path_file_source, path_file_dest, job_name):
    
    """
    Esta función permite transformar un archivo en formato .csv a formato .pqt usando 
    la herramient glue del datalake. Ademas hace el movimiento entre las zonas del 
    datalake si es necesario
    
    Uso:
        transformarCsvPqtDatalake("s3://landing-zone-analitica/xxxx-analitica/holamundojupyter.csv", "s3://raw-zone-analitica/xxxx-analitica/holamundo.pqt","xxxx-analitica")
    """
    import sys
    import datetime
    from time import sleep
    import pandas as pd
    import boto3
    from botocore.errorfactory import ClientError
    
    def fecha():
        return datetime.datetime.now().strftime("%m/%d/%y, %H:%M:%S")
    
    
    glue = boto3.client('glue', region_name="us-east-1")
        
    glue.create_job(
        Name=job_name,
        Role='AWSGlueServiceRoleDefaultSura',
        Command={'Name': 'glueetl',
                 'ScriptLocation': 's3://script-glue-analitica/martin.arrieta/csv_to_pqt_no_catalog.py'
                },
        MaxCapacity=2
    )
    
    
    job_start_resp = glue.start_job_run(
            JobName = job_name,
            Arguments={
                '--origin_path': path_file_source,
                '--dest_path': path_file_dest
            },
            MaxCapacity=2
        )
    
    job_run_id = job_start_resp['JobRunId']
    
    #print("job_run_id: ", job_run_id)

    sleep(10)
    try:
        print ("Ini Job: " + job_name + ',' + fecha())
        
        while True:
            sleep(5)
            job_run_resp = get_job_run_resp=glue.get_job_run(
                                JobName=job_name,
                                RunId=job_run_id,
                            )
            print("JobRunState: ", get_job_run_resp['JobRun']['JobRunState'])
            
            curated_state = get_job_run_resp['JobRun']['JobRunState']
         
            if curated_state != 'RUNNING': 
                sleep(30)
                print ("Fin Job: " + job_name + ',' + fecha())
                break
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConcurrentRunsExceededException':
            print ("--------------- Falló: Job continua corriendo")
            error_state = get_job_run_resp['JobRun']['ErrorMessage']
            print("Failed: ", error_state)
        else:
            #log.exception(e)
            print "Job already running", exception(e)#Change
            raise e