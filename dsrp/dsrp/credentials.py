import os

key_1 = {'IAM_SERVICE_ID':  str(os.environ.get('IBM_KEY_1_IAM_SERVICE_ID')),
         'IBM_API_KEY_ID':  str(os.environ.get('IBM_KEY_1_IBM_API_KEY_ID')),
         'ENDPOINT':  str(os.environ.get('IBM_KEY_1_ENDPOINT')),
         'IBM_AUTH_ENDPOINT':  str(os.environ.get('IBM_KEY_1_IBM_AUTH_ENDPOINT')),
         'BUCKET':  str(os.environ.get('IBM_KEY_1_BUCKET')),
         # 'FILE':  str(os.environ.get('IBM_KEY_1_FILE'))
         }

key_2 = {"apikey":  str(os.environ.get('IBM_KEY_2_APIKEY')),
         "endpoints":  str(os.environ.get('IBM_KEY_2_ENDPOINTS')),
         "iam_apikey_description":  str(os.environ.get('IBM_KEY_2_IAM_APIKEY_DESCRIPTION')),
         "iam_apikey_name":  str(os.environ.get('IBM_KEY_2_IAM_APIKEY_NAME')),
         "iam_role_crn":  str(os.environ.get('IBM_KEY_2_IAM_ROLE_CRN')),
         "iam_serviceid_crn":  str(os.environ.get('IBM_KEY_2_IAM_SERVICEID_CRN')),
         "resource_instance_id":  str(os.environ.get('IBM_KEY_2_RESOURCE_INSTANCE_ID'))
         }

key_3 =  str(os.environ.get('MONGODB_SRV'))
