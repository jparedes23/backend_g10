from django.contrib import admin
from .models import ProductosModel

## para mostrar los campos en el admin
class ShowFields(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'estado')

admin.site.register(ProductosModel, ShowFields)


