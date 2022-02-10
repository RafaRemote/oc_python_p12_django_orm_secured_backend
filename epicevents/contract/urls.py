from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("contract", views.ContractViewSet, basename="contract")

urlpatterns = [path("", include(router.urls))]
