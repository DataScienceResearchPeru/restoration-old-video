import ibm_boto3
from ibm_botocore.client import Config
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
###########################################################
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
###########################################################


# from .models import ProductoHijoCompra
# from .models import ProductoPadre
# from .models import Proveedor
# from .models import BoletaCompra
# ###########################################################
# from .models import ProductoPlato
# from .models import PlatoPadre
# from .models import PlatoHijoVenta
# from .models import BoletaVentaRestaurante
# from .models import ProductoHijoTransaccion


###########################################################
from django.utils.timezone import get_current_timezone
import datetime
##########################################################
from django.db.models import Count
from django.db.models import Sum
from django.db.models import F

##########################################################
# Allow iFrame
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin

##########################################################
# ALLOW REST_FRAMEWORK LOGIN
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
# from .models import AuthtokenToken
# from .models import AuthUser
# from .models import ApiMedicKitPerUser
from .forms import SignUpForm
from django.contrib import messages

##########################################################
# ALLOW WEBHOOK GRAFANA
# from .models import ApiMedicNotifications
from django.utils import timezone
from rest_framework.utils import json


##########################################################
# ALLOW MONGODB
import pymongo
from pymongo import MongoClient
from bson import objectid
from bson.objectid import ObjectId
from datetime import datetime
import pprint
##################################
from .forms import VideoForm
import os
import subprocess


# -------------------- INICIO CREDENTIALS -----------------

credentials = {
    'IAM_SERVICE_ID': 'iam-ServiceId-b426f19e-8df6-45b8-9c4d-37893e41f238',
    'IBM_API_KEY_ID': '3aNvqt_qMzCDtV8pzuWTpE_ZCePUFP_ICel2L61caQfD',
    'ENDPOINT': 'https://s3-api.us-geo.objectstorage.service.networklayer.com',
    'IBM_AUTH_ENDPOINT': 'https://iam.cloud.ibm.com/oidc/token',
    'BUCKET': 'dsrp-donotdelete-pr-dhxpvvck0joofu',
    # 'FILE': 'frames_out.zip'
}

cos_credentials = {
    "apikey": "zc4cz12_i6iTStQFwlTv0wxHphEEY8NVqNb6U4BY749o",
    "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
    "iam_apikey_description": "Auto-generated for key 160374f5-9c1f-4273-a772-0f787b4eb2da",
    "iam_apikey_name": "rovdsrp",
    "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
    "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/bf08352255e54408bc6145b47bf34ff9::serviceid:ServiceId-5f3686ab-205e-4c10-9f15-691a51f426eb",
    "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/bf08352255e54408bc6145b47bf34ff9:70cf7ab6-2002-456f-adff-87469270a801::"
}

auth_endpoint = 'https://iam.bluemix.net/oidc/token'
service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'
cos = ibm_boto3.client('s3',
                       ibm_api_key_id=cos_credentials['apikey'],
                       ibm_service_instance_id=cos_credentials['resource_instance_id'],
                       ibm_auth_endpoint=auth_endpoint,
                       config=Config(signature_version='oauth'),
                       endpoint_url=service_endpoint)


def upload_file_cos(credentials, local_file_name, key):
    cos = ibm_boto3.client(service_name='s3',
                           ibm_api_key_id=credentials['IBM_API_KEY_ID'],
                           ibm_service_instance_id=credentials['IAM_SERVICE_ID'],
                           ibm_auth_endpoint=credentials['IBM_AUTH_ENDPOINT'],
                           config=Config(signature_version='oauth'),
                           endpoint_url=credentials['ENDPOINT'])
    try:
        res = cos.upload_file(Filename=local_file_name,
                              Bucket=credentials['BUCKET'], Key=key)
    except Exception as e:
        print(Exception, e)
    else:
        print('File Uploaded')


def download_file_cos(credentials, local_file_name, key):
    cos = ibm_boto3.client(service_name='s3',
                           ibm_api_key_id=credentials['IBM_API_KEY_ID'],
                           ibm_service_instance_id=credentials['IAM_SERVICE_ID'],
                           ibm_auth_endpoint=credentials['IBM_AUTH_ENDPOINT'],
                           config=Config(signature_version='oauth'),
                           endpoint_url=credentials['ENDPOINT'])
    try:
        res = cos.download_file(
            Bucket=credentials['BUCKET'], Key=key, Filename=local_file_name)
    except Exception as e:
        print(Exception, e)
    else:
        print('File Downloaded')

# cos.upload_file(Filename='results/frames_out_fastdvdnet.zip',Bucket=credentials['BUCKET'],Key='frames_out_fastdvdnet.zip')
# cos.download_file(Bucket=credentials['BUCKET'],Key='frames_out.zip',Filename='frames_out.zip')


def get_mongo_client():
    return MongoClient("mongodb+srv://dsrpbetamongodb:dsrpbetamongodb@cluster0.ko3xv.gcp.mongodb.net/galeria?retryWrites=true&w=majority")
# -------------------- FIN CREDENTIALS -----------------


# ------------------------  INICIO LOGIN ------------------
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(
                request, 'Nueva cuenta registrada satisfactoriamente.')
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

# ------------------------  FIN LOGIN ------------------

# ------------------------ INICIO INDEX ------------------


def index_view(request):

    # Variables de reporte mensual

    return render(request, 'index/index.html', locals())

# -------------------------- FIN INDEX -------------------

# -------------------- INICIO DASHBOARD -----------------


def handle_uploaded_file(f, codigo, current_user_id):

    temp_file_dir = 'dsrp/static/temp_upload/' + \
        str(datetime.now().strftime('%Y%m%d%H%M%S')) + \
        "-"+str(current_user_id)+"-" + f.name

    temp_file_dir2 = 'static/temp_upload/' + \
        str(datetime.now().strftime('%Y%m%d%H%M%S')) + \
        "-"+str(current_user_id)+"-" + f.name

    static_file_dir = '/temp_upload/' + \
        str(datetime.now().strftime('%Y%m%d%H%M%S')) + \
        "-"+str(current_user_id)+"-" + f.name

    # if not os.path.isdir('dsrp/static/temp_upload/'):
    #     os.mkdir('dsrp/static/temp_upload/')
    try:
        with open(temp_file_dir, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    except Exception as e:  # Exclusive for Heroku
        with open('app/'+temp_file_dir2, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    name_file_cos = str(datetime.now().strftime('%Y%m%d%H%M%S')) + \
        "-"+str(current_user_id)+"-"+codigo + '.mp4'

    cos.upload_file(Filename=temp_file_dir,
                    Bucket=credentials['BUCKET'], Key=name_file_cos)

    print("File uploaded to IBM COS")

    client = MongoClient(
        "mongodb+srv://dsrpbetamongodb:dsrpbetamongodb@cluster0.ko3xv.gcp.mongodb.net/galeria?retryWrites=true&w=majority")
    db = client.galeria
    collection = db.videos

    data = {'current_user_id': str(current_user_id),
            'filename_temp': str(temp_file_dir),
            'filename_cos': str(name_file_cos),
            'static_file_dir': str(static_file_dir),
            'temp_file_dir2':str(temp_file_dir2),
            }
    print(data)

    collection.insert_one(data)


@csrf_exempt
@login_required(login_url='/accounts/login')
@permission_classes((AllowAny,))
def dashboard_upload_view(request):

    if request.method == "POST":

        video = VideoForm(request.POST, request.FILES)
        if video.is_valid():
            current_user_id = request.user.id
            handle_uploaded_file(
                request.FILES['video'], request.POST.get('codigo'), current_user_id)
            print("File uploaded successfuly")
            HttpResponse("File uploaded successfuly")
            return redirect('../status/')

    else:
        video = VideoForm()
        return render(request, 'dashboard/pipeline/upload.html', {'form': video, 'user_name': str(request.user.username)})


@login_required(login_url='/accounts/login')
def dashboard_status_view(request):

    current_user_id = request.user.id
    # Variables de dashboard

    client = MongoClient(
        "mongodb+srv://dsrpbetamongodb:dsrpbetamongodb@cluster0.ko3xv.gcp.mongodb.net/galeria?retryWrites=true&w=majority")
    db = client.galeria
    collection = db.videos

    # files=collection.find({'current_user_id':current_user_id})
    # # GET FILE ID
    # print("GETTING FILE ID")
    list_filename_temp = []
    myvideos = collection.find({'current_user_id': str(current_user_id)})
    # for myvid in myvideos:
    #     list_filename_temp.append(myvideos['static_file_dir'])

    list_filename_temp.append(myvideos[0]['static_file_dir'])

    # list_filename_temp

    # # GET CHUNKS OF THE FILE WITH ID
    # print("GET CHUNKS OF THAT FILE")
    # files_id = ObjectId('5f67ee7920bfdaf148938ccd')
    # thefile = []
    # for chunk in cluster_db['uploaded_videos']['chunks'].find({"files_id": files_id}):
    #     thefile.append(chunk['data'])
    #     pprint.pprint(chunk['_id'])

    path='./'

    return render(request, 'dashboard/pipeline/status.html', locals())



@login_required(login_url='/accounts/login')
def dashboard_utils_view(request):

    myCmd = "ls"
    listoffiles=str(subprocess.check_output(myCmd, shell=True).decode("utf-8"))

    myCmd2 = "ls ../"
    listoffiles2=str(subprocess.check_output(myCmd2, shell=True).decode("utf-8"))

    try:
        myCmd3 = "ls ./static/"
        listoffiles3=str(subprocess.check_output(myCmd3, shell=True).decode("utf-8"))
    except Exception as e:
        listoffiles3=str(e)
        print(e)
    
    try:
        myCmd4 = "ls ./static/temp_upload/"
        listoffiles4=str(subprocess.check_output(myCmd4, shell=True).decode("utf-8"))
    except Exception as e:
        listoffiles4=str(e)
        print(e)

    return render(request, 'dashboard/pipeline/utils.html', locals())

# ----------------------- FIN DASHBOARD -----------------

# -------------------- INICIO LOGIN REST_FRAMEWORK -----------------

# -------------------- FIN LOGIN REST_FRAMEWORK -----------------
