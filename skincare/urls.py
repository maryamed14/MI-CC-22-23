from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views

from .views import PersonViewSet
#router = DefaultRouter(trailing_slash=False)

router = routers.DefaultRouter()
router.register(r'skincare', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
