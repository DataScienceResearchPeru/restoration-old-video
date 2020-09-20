from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
###########################################################
from django.shortcuts import redirect, render
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
from gridfs import GridFS
from bson import objectid


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

@login_required(login_url='/accounts/login')
def dashboard_upload_view(request):

    # Variables de dashboard
    try:
        cluster_db = MongoClient(
            "mongodb+srv://dsrpbetamongodb:dsrpbetamongodb@cluster0.ko3xv.gcp.mongodb.net/videos?retryWrites=true&w=majority").videos
        print("client connected")

        fs = GridFS(cluster_db, "uploaded_videos")
        with open('dsrp/static/temp_upload/my_video_source.mp4', 'rb') as f:
            uploaded_videos = fs.put(f.read(), content_type='video/mp4', filename='my_video_source.mp4', encoding='utf-8')
        
        print("File uploaded")

    except Exception as e:
        print(e)

    return render(request, 'dashboard/pipeline/upload.html', locals())

@login_required(login_url='/accounts/login')
def dashboard_status_view(request):

    # Variables de dashboard

    return render(request, 'dashboard/pipeline/status.html', locals())


# ----------------------- FIN DASHBOARD -----------------

# -------------------- INICIO LOGIN REST_FRAMEWORK -----------------

# -------------------- FIN LOGIN REST_FRAMEWORK -----------------
