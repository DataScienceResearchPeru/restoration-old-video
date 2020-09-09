# myapi/urls.py
from django.urls import include, path
from rest_framework import routers

# from .views import medichypertableViewSet
# from .views import lastmedichypertableViewSet

# from .views import get_kit_data_view

router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)
# router.register(r'all_data',medichypertableViewSet,'all_data')
# router.register(r'last_data',lastmedichypertableViewSet,'last_data')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('last_data_by_user/',get_kit_data_view,name='last_data_by_user'),
]