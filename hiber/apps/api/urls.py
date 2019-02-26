from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from . import views

schema_view = get_schema_view(title='Bat House API')

router = DefaultRouter()
router.register(r'bat', views.BatViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]
