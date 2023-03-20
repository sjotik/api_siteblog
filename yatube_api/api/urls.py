from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1 .register(r'posts', PostViewSet, basename='post')
router_v1 .register(r'groups', GroupViewSet, basename='group')
router_v1 .register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1 .urls), name='api-root')
]
