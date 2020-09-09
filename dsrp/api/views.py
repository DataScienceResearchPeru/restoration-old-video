# views.py
from rest_framework import viewsets

# from api.serializers import HeroSerializer
# from .serializers import medichypertableSerializer
# from .serializers import lastmedichypertableSerializer
# from .serializers import lastmedicbykitidhypertableSerializer
# from api.models import Hero
# from .models import ApiMedicHypertable

##########################################################
# ALLOW REST_FRAMEWORK LOGIN
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from dsrp.models import AuthtokenToken
from dsrp.models import AuthUser
from dsrp.models import ApiMedicKitPerUser
from rest_framework.response import Response
from django.http import JsonResponse

# ENDPOINTS WITH TABLES


# class medichypertableViewSet(viewsets.ModelViewSet):
#     queryset = ApiMedicHypertable.objects.all().order_by('time')
#     serializer_class = medichypertableSerializer


# class lastmedichypertableViewSet(viewsets.ModelViewSet):
#     queryset = ApiMedicHypertable.objects.all().order_by('-time')[:1]
#     serializer_class = lastmedichypertableSerializer

# ENDPOINTS WITH TOKENS
# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def get_kit_data_view(request):

#     token = request.data.get("token")
#     if token is None:
#         return Response({'error': 'Porfavor envia un token válido'}, status=HTTP_400_BAD_REQUEST)
#     user_by_token = AuthtokenToken.objects.get(pk=token)
#     user_kit_id = ApiMedicKitPerUser.objects.get(user_id=user_by_token.user_id)
#     data=ApiMedicHypertable.objects.filter(kit_id=user_kit_id.kit_id).order_by('-time')[:1].values()

#     return Response(list(data), status=HTTP_200_OK)
