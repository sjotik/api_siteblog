import imp
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, PostViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls), name='api-root')
]
