# Register your models here.
from django.contrib.gis import admin
from markers.models import Toponym


@admin.register(Toponym)
class ToponymAdmin(admin.GISModelAdmin):
    """Toponyms admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "photo","audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import LineToponym
@admin.register(LineToponym)
class LineToponymAdmin(admin.GISModelAdmin):
    """Toponyms admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "photo","audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Monument
@admin.register(Monument)
class MonumentAdmin(admin.GISModelAdmin):
    """Monuments admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "photo","audio")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class ToponymInline(admin.TabularInline):
    model = Toponym
class MonumentInline(admin.TabularInline):
    model = Monument
from markers.models import Municipal
@admin.register(Municipal)
class MunicipalAdmin(admin.GISModelAdmin):
    """Municipals admin."""
    inlines = [
        ToponymInline,
        MonumentInline,
    ]
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {  
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "mpoly", "area")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Battle
@admin.register(Battle)
class BattleAdmin(admin.GISModelAdmin):
    """Battle admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "year", "regiments")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class BattleInline(admin.TabularInline):
    model = Battle
from markers.models import Regiment
@admin.register(Regiment)
class RegimentAdmin(admin.GISModelAdmin):
    """Regiment admin."""
    inlines = [
        BattleInline,
    ]
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "period", "place", "size", "commander")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Route
@admin.register(Route)
class RouteAdmin(admin.GISModelAdmin):

    """Route admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "length", "duration", "regiment")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Fort
@admin.register(Fort)
class FortAdmin(admin.GISModelAdmin):
    """Fort admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location", "description", "battles", "longitude", "latitude")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Cities
@admin.register(Cities)
class CitiesAdmin(admin.GISModelAdmin):
    """Cities admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "location")
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
from markers.models import Uezd
@admin.register(Uezd)
class UezdAdmin(admin.GISModelAdmin):
    """Uezd admin."""
    #Задаем начальное положение карты
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lon': 55.9678,
            'default_lat': 54.7431,
        },
    }
    list_display = ("name", "description", "photo", "audio", "video", "amenity", "amenity1")