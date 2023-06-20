"""Markers models."""

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

class Toponym(models.Model): #топонимы
    name = models.CharField(max_length=255) #описывает имя объекта длиной 255
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431))
    place = models.CharField(blank=True, max_length=255,null=True) #описывает местоположение
    description = models.TextField(blank=True, max_length= 2000,null=True) #описание
    audio = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    municipals = models.ForeignKey('Municipal',null=True, blank=True, on_delete=models.SET_NULL)
    amenity = models.CharField(max_length=255, default="Монумент", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="toponym", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        """Return string representation."""
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class LineToponym(models.Model): #топонимы линии
    name = models.CharField(max_length=255) #описывает имя объекта длиной 255
    location = models.MultiLineStringField(null=True) #задает локацию
    description = models.TextField(blank=True, max_length= 2000,null=True) #описание
    audio = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    toponyms = models.ForeignKey('Toponym',null=True, blank=True, on_delete=models.SET_NULL)
    municipals = models.ForeignKey('Municipal',null=True, blank=True, on_delete=models.SET_NULL)
    amenity = models.CharField(max_length=255, default="Монумент", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="toponym", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        """Return string representation."""
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Monument(models.Model): #памятник
    name = models.CharField(max_length=255) #описывает имя объекта длиной 255
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431))
    description = models.TextField(blank=True, max_length= 2000,null=True) #описание
    architect = models.CharField(blank=True, max_length=255,null=True)
    year = models.CharField(blank=True, max_length=255,null=True)
    municipals = models.ForeignKey('Municipal',null=True, blank=True, on_delete=models.SET_NULL) #задает внешний ключ Pamyatniki, при удалении из первичной таблицы, запись во вторичной принимает значение NULL
    amenity = models.CharField(max_length=255, default="Памятник", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="monument", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Municipal(models.Model): #муниципальные районы
    name = models.CharField(max_length=255)
    mpoly = models.MultiPolygonField()
    amenity = models.CharField(max_length=255, default="Муниципальный район", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="Municipal", editable = False) #описывает имя объекта длиной 255
    area = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Regiment(models.Model): #полк
    name = models.CharField(max_length=255)
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431))
    period = models.TextField(blank=True, max_length= 1000,null=True) #период существования
    place = models.CharField(blank=True, max_length= 255,null=True) #место формирования
    size = models.TextField(blank=True, max_length= 1000,null=True) #численность
    commander = models.TextField(blank=True, max_length= 500,null=True) #командир
    amenity = models.CharField(max_length=255, default="Полк", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="regiment", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Battle(models.Model): #сражения
    name = models.CharField(max_length=255)
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431))
    description = models.TextField(blank=True, max_length= 2000,null=True) #описание
    year = models.DateField(blank=True, null=True)
    regiments = models.ForeignKey('Regiment',null=True, blank=True, on_delete=models.SET_NULL)
    amenity = models.CharField(max_length=255, default="Сражение", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="battle", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    def __str__(self):
        return self.description
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Route(models.Model): #маршрут
    name = models.CharField(max_length=255)
    location = models.MultiLineStringField(null=True) #задает локацию
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    regiment = models.ForeignKey('Regiment',null=True, blank=True, on_delete=models.SET_NULL)
    amenity = models.CharField(max_length=255, default="Маршрут", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="route", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Fort(models.Model): #крепости
    name = models.CharField(max_length=255)
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431))
    latitude = models.CharField(max_length=255, null=True, editable = False) #описывает имя объекта длиной 255
    longitude = models.CharField(max_length=255, null=True, editable = False) #описывает имя объекта длиной 255
    description = models.TextField(blank=True, max_length= 2000,null=True) #описание
    battles = models.ForeignKey('Battle',null=True, blank=True, on_delete=models.SET_NULL)
    amenity = models.CharField(max_length=255, default="Крепость", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="fort", editable = False) #описывает имя объекта длиной 255
    audio = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Cities(models.Model): #города
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431))
    name = models.CharField(max_length=255)
    amenity = models.CharField(max_length=255, default="Город", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="cities", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Uezd(models.Model): #уездные города
    name = models.CharField(max_length=255)
    location = LocationField(zoom=7, default=Point(55.9678, 54.7431))
    description = models.TextField(blank=True, max_length= 2000,null=True) #описание
    audio = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    photo = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    video = models.CharField(blank=True, max_length=2000,default="") #ссылка на web страницу без https
    amenity = models.CharField(max_length=255, default="Уезд", editable = False) #описывает имя объекта длиной 255
    amenity1 = models.CharField(max_length=255, default="uezd", editable = False) #описывает имя объекта длиной 255
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Mesh1(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Mesh2(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk1(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk2(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk3(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk4(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk5(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk6(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk7(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk8(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk9(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk10(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk11(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk12(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk13(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk14(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk15(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk16(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk17(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk18(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk19(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name
#--------------------------------------#
#--------------------------------------#
#--------------------------------------#
class Polk20(models.Model): #маршрут
    location = models.MultiLineStringField(null=True) #задает локацию
    polk = models.CharField(max_length=255)
    otkuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    kuda = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    duration = models.CharField(blank=True,max_length= 255,null=True) #продолжительность
    length = models.CharField(blank=True, max_length= 255,null=True) #протяженность
    def __str__(self):
        return self.name