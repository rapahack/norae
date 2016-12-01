import sys
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Articulo, Categoria

# Create your views here.
def IndexView(request):
	return render(request, 'index.html')

def ArticuloView(request):
    template_name = 'blog.html'
    model = Articulo
    
    articulos = Articulo.objects.all()
    categorias = Categoria.objects.all()
    
    data = {'articulos': articulos,'categorias' : categorias}
    return render(request, 'blog.html', data)
    # en lugar de que diga object_list en la plantilla
    # context_object_name = "articulo"

def CategoriasView(request):
    template_name = 'articulo.html'
    model = Articulo

    articulos = Articulo.objects.all()
    categorias = Categoria.objects.all()
    descripcion = Categoria.objects.all()

    data = {'articulos': articulos, 'categorias' : categorias}
    return render(request, 'articulo.html', data)
    # en lugar de que diga object_list en la plantilla
    # context_object_name = "articulo"
def listing(request, idc):
    categoria = Categoria.objects.get(pk=idc)
    articulo_list = Articulo.objects.filter(categoria=categoria)
    paginator = Paginator(articulo_list, 4) # Show 10 articulos per page

    page = request.GET.get('page')
    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articulos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articulos = paginator.page(paginator.num_pages)

    data = {'articulos': articulos, 'categoria': categoria, 'articulo_list' : articulo_list}
    return render(request, 'blog.html', data)

