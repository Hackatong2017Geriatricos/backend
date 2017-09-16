from django.contrib import admin
from api.models import Local, LocalOrigenDatos, OrigenDatos, Imagen

# Register your models here.

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    field = ('local', 'url')

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    field = ('origen_referencia', 'nombre', 'descripcion')


@admin.register(LocalOrigenDatos)
class LocalOrigenDatosAdmin(admin.ModelAdmin):
    fields = ('id_referencia', 'origen')


@admin.register(OrigenDatos)
class OrigenDatosAdmin(admin.ModelAdmin):
    fields = ('nombre', 'url')
