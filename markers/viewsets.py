"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Toponym
from markers.serializers import ToponymSerializer


class ToponymViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Toponym.objects.all()
    serializer_class = ToponymSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import LineToponym
from markers.serializers import LineToponymSerializer


class LineToponymViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = LineToponym.objects.all()
    serializer_class = LineToponymSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument
from markers.serializers import MonumentSerializer


class MonumentViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Monument.objects.all()
    serializer_class = MonumentSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Municipal
from markers.serializers import MunicipalSerializer


class MunicipalViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Municipal.objects.all()
    serializer_class = MunicipalSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Regiment
from markers.serializers import RegimentSerializer


class RegimentViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Regiment.objects.all()
    serializer_class = RegimentSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Battle
from markers.serializers import BattleSerializer


class BattleViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#    
from markers.models import Route
from markers.serializers import RouteSerializer


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Fort
from markers.serializers import FortSerializer


class FortViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Fort.objects.all()
    serializer_class = FortSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Cities
from markers.serializers import CitiesSerializer


class CitiesViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Uezd
from markers.serializers import UezdSerializer


class UezdViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Uezd.objects.all()
    serializer_class = UezdSerializer
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#