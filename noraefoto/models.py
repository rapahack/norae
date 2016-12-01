from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib import admin

class Categoria(models.Model):
	categoria = models.TextField(max_length=50)
	imagen = models.ImageField(upload_to='categorias', default='categoria.png')
	descripcion = models.TextField(max_length=300, default="")
	
	def __unicode__(self):
		return self.categoria

class Articulo(models.Model):
	categoria= models.ForeignKey(Categoria)
	titulo = models.TextField(max_length=50)
	imagen = models.ImageField(upload_to='fotos', default='fotodefault.png')
	detalles = models.TextField(max_length=100500, default="")
	fecha = models.DateTimeField(auto_now_add=True)
	descripcion = models.TextField(max_length=1500, default="")
                                                           
	def __unicode__(self):
		return self.titulo
    
