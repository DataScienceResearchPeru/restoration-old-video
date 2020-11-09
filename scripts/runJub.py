import sys
import urllib3, requests, json
from time import sleep
import requests, os

params = {}
params['apikey'] = "APIKEY DE IBM CLOUD"
params['token_url'] = "https://iam.cloud.ibm.com/oidc/token"
params['token_data'] = "apikey=" + params['apikey'] + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
params['token_headers'] = { "Content-Type" : "application/x-www-form-urlencoded"}
params['project_id'] = "PROJECT_ID LO OBTIENES DE WATSON STUDIO CON EL TOKEN"
    
# create a new bearer token 
iam_response  = requests.post(params['token_url'], headers=params['token_headers'], data=params['token_data'])
bearer_token = "Bearer " + iam_response.json()["access_token"]

# Definiendo el jobrunpost
jobrunpost = {
  "job_run": {
      "configuration" : {
          "env_variables" :  [] 
      }
  }
}

# Wrapper for REST API calls
def callrest(method,request,postdata=None):
    url = 'https://api.dataplatform.cloud.ibm.com'
    headers = {
        'Authorization': bearer_token,
        'Content-Type': 'application/json'
    }

    if method == "POST" :
        print("POST",url+request,postdata)
        response = requests.post(url+request, json=postdata, headers=headers, verify=False)
    else:
        print("GET",url+request)
        response = requests.get(url+request, headers=headers, verify=False)

    print("status",response.status_code )
    if response.status_code != 200 and response.status_code != 201:
        print('Request failed.')
        raise Exception(response.text)
    return response.json()

def job_asset(nombre_job):
    ##Llamando a todos los jobs
    jobs = callrest("GET","/v2/jobs?project_id="+ params['project_id'])
    
    ##Obteniendo info del job indicado
    MyJobName=nombre_job
    myjob = next(job for job in jobs['results'] if job['metadata']['name']==MyJobName)
    
    ##Obteniendo el job_asset_id
    job_asset_id=myjob['metadata']['asset_id']
    
    return job_asset_id
    
def main(dict):
    
    ##Obteniendo el job_asset_id
    job_asset_id = job_asset('NOMBRE DEL JOB')
    
    ##Ejecutando el job -> job-nb-prep-vmm-model
    jobrun = callrest("POST","/v2/jobs/"+job_asset_id+"/runs?project_id="+params['project_id'], jobrunpost)
    
    ##Obteniendo job_run_id
    job_run_id = jobrun['metadata']['asset_id']
    
    ##Ejecutando el while hasta que termine de ejecutar el primer job
    while True:
        sleep(30)
        # Check status of Job Run, e.g. 'Starting', 'Running', 'Completed', 'Failed', 'Canceled'
        status = callrest("GET","/v2/jobs/"+job_asset_id+"/runs/"+job_run_id+"?project_id="+params['project_id'])
        #print(status['entity']['job_run']['state'])
        if status['entity']['job_run']['state'] in ['Completed', 'Failed', 'Canceled']:
            break;


    return status
    



