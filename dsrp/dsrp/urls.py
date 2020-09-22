"""dsrp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# Heroku
from django.conf import settings
from django.conf.urls.static import static

# Login
from .views import signup

# Pages
from .views import index_view
from .views import dashboard_upload_view
from .views import dashboard_status_view
from .views import dashboard_utils_view
# Oauth



urlpatterns = [

    path('admin/', admin.site.urls),
    # -----------------INICIO LOGIN----------------
    path('accounts/', include('django.contrib.auth.urls')), # No register auth builded
    url(r'^accounts/register/$',signup,name='signup'),
    # -----------------FIN LOGIN----------------

    # -----------------INICIO INDEX----------------
    path('', index_view, name='main-view'),
    # path('pdp/', pdp_view, name='pdp'),
    # ------------------FIN INDEX------------------
    # -----------------INICIO DASHBOARD----------------
    path('dashboard/upload/', dashboard_upload_view, name='dashboard-upload-view'),
    path('dashboard/status/', dashboard_status_view, name='dashboard-status-view'),
    path('dashboard/utils/', dashboard_utils_view, name='dashboard-utils-view'),
    
    # path('dashboard/estadisticas_a_detalle/alertas_emitidas/', alertas_emitidas_view, name='alertas-detalle-view'),
    # path('dashboard/estadisticas_a_detalle/lista_dispositivos_operativos/', lista_dispositivos_operativos_view, name='lista-dispositivos-operativos-view'),    
    # path('dashboard/personal/', informacion_tiempo_real_view, name='informacion-tiempo-real-view'),


    # path('personal/', personal_view, name='personal-view'),
    # ------------------FIN DASHBOARD------------------
    # -----------------INICIO API----------------
    path('api/', include('api.urls')),
    # ------------------FIN API------------------

    # -----------------INICIO OAUTH----------------
    path('auth2/', include('rest_framework_social_oauth2.urls')),
    # path('auth/login/', login_rest_framework_view, name='login_auth_rest_framework'),
    # path('auth/logged/get_data_user/', get_name_rest_framework_view, name='get_data_user_rest_framework'),
    # path('auth/logged/get_user_kit_data/', get_kit_data_view, name='get_user_kit_data'),
    # path('auth/logged/get_notifications_per_kit_id/',get_notifications_per_kit_id_view,name='get_notifications_per_kit_id'),

    # -----------------FIN OAUTH----------------


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
