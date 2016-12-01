from django.contrib import admin

# Register your models here.
from django.conf import settings
from .models import Articulo, Categoria

admin.site.register(Articulo)
admin.site.register(Categoria)