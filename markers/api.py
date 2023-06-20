"""Markers API URL Configuration."""

from rest_framework import routers
router = routers.DefaultRouter()
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import ToponymViewSet
router.register(r"toponyms", ToponymViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import LineToponymViewSet
router.register(r"linetoponym", LineToponymViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import MonumentViewSet
router.register(r"monuments", MonumentViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import MunicipalViewSet
router.register(r"municipals", MunicipalViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import RegimentViewSet
router.register(r"regiments", RegimentViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import BattleViewSet
router.register(r"battles", BattleViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import RouteViewSet
router.register(r"routes", RouteViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import FortViewSet
router.register(r"forts", FortViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import CitiesViewSet
router.register(r"city", CitiesViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.viewsets import UezdViewSet
router.register(r"uezds", UezdViewSet)
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
urlpatterns = router.urls