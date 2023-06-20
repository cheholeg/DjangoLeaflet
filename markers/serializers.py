"""Markers serializers."""

from rest_framework_gis import serializers
from rest_framework import serializers as serial
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Toponym

class ToponymSerializer(serializers.GeoFeatureModelSerializer): # ТОПОНИМЫ
    """Toponym GeoJSON serializer."""
    class Meta:
        """Toponym serializer meta class."""

        fields = ("id", "name", "description", "amenity", "amenity1", "photo", "audio", "video", "place")
        geo_field = "location"
        model = Toponym
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import LineToponym

class LineToponymSerializer(serializers.GeoFeatureModelSerializer): # ТОПОНИМЫ ЛИНИИ
    """Toponymline GeoJSON serializer."""

    class Meta:
        """Toponymline serializer meta class."""

        fields = ("id", "name", "description", "amenity", "amenity1", "photo", "audio", "video")
        geo_field = "location"
        model = LineToponym        
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument

class MonumentSerializer(serializers.GeoFeatureModelSerializer): # ПАМЯТНИКИ
    """Monument GeoJSON serializer."""

    class Meta:
        """Monument serializer meta class."""

        fields = ("id", "name", "description", "architect", "year", "amenity", "amenity1", "photo", "audio", "video")
        geo_field = "location"
        model = Monument
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Municipal

class MunicipalSerializer(serializers.GeoFeatureModelSerializer): # Муниципальный районы
    """Municipal GeoJSON serializer."""
    toponym_set = serial.StringRelatedField(many=True)
    monument_set = serial.StringRelatedField(many=True)
    class Meta:
        """Municipal serializer meta class."""

        fields = ("id", "name", "area", "amenity", "amenity1", 'toponym_set', 'monument_set')
        geo_field = "mpoly"
        model = Municipal
        
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Regiment

class RegimentSerializer(serializers.GeoFeatureModelSerializer): # ПОЛКИ
    """Regiment GeoJSON serializer."""
    battle_set = serial.StringRelatedField(many=True)
    class Meta:
        """Regiment serializer meta class."""

        fields = ("id", "name", "period", "place", "size", "commander", "photo", "audio", "video", "amenity", "amenity1", "battle_set")
        geo_field = "location"
        model = Regiment
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Battle

class BattleSerializer(serializers.GeoFeatureModelSerializer): # Сражения
    """Battle GeoJSON serializer."""

    class Meta:
        """Battle serializer meta class."""

        fields = ("id", "name", "description", "year", "regiments", "photo", "audio", "video", "amenity", "amenity1")
        geo_field = "location"
        model = Battle
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Route

class RouteSerializer(serializers.GeoFeatureModelSerializer): # Маршруты
    """Route GeoJSON serializer."""

    class Meta:
        """Route serializer meta class."""

        fields = ("id", "name", "length", "duration", "regiment", "photo", "audio", "video", "amenity", "amenity1")
        geo_field = "location"
        model = Route
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Fort

class FortSerializer(serializers.GeoFeatureModelSerializer): # Крепости
    """Route GeoJSON serializer."""

    class Meta:
        """Fort serializer meta class."""

        fields = ("id", "name", "description", "battles", "photo", "audio", "video", "amenity", "amenity1", "longitude", "latitude")
        geo_field = "location"
        model = Fort
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Cities

class CitiesSerializer(serializers.GeoFeatureModelSerializer): # Города
    """Cities GeoJSON serializer."""

    class Meta:
        """Cities serializer meta class."""

        fields = ("id", "name", "amenity", "amenity1")
        geo_field = "location"
        model = Cities
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Uezd

class UezdSerializer(serializers.GeoFeatureModelSerializer): # Уезды
    """Uezd GeoJSON serializer."""

    class Meta:
        """Uezd serializer meta class."""

        fields = ("id", "name", "description", "photo", "audio", "video", "amenity", "amenity1")
        geo_field = "location"
        model = Uezd