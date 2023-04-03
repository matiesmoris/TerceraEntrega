from django.shortcuts import render
from django.http import HttpResponse
from Entrega3.models import Tarea, Persona, Producto
from Entrega3.forms import PersonaForm, BuscarPersonasForm, ProductoForm, BuscarProductosForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
def mostrar_mis_tareas(request, criterio):
    
    if criterio == "todo":
        tareas = Tarea.objects.all()
    else:
        tareas = Tarea.objects.filter(nombre=criterio).all()

    return render(request, "Entrega3/tareas.html", {"tareas": tareas})


def mostrar_personas(request):
    
    personas = Persona.objects.all()
    total_personas = len(personas)
    context = {
        "personas": personas, 
        "total_personas":total_personas,
        "form": PersonaForm(),
    }
    return render(request, "Entrega3/personas.html", context)


def crear_persona(request):

    f = PersonaForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Persona(nombre=f.data["nombre"], apellido=f.data["apellido"], fecha_nacimiento=f.data["fecha_nacimiento"]).save()
        context['form'] = PersonaForm()

    context["personas"] = Persona.objects.all()
    context["total_personas"] = len(Persona.objects.all())
         
    return render(request, "Entrega3/personas.html", context)


class BuscarPersonas(ListView):
    model = Persona
    context_object_name = "personas"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
           return Persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Persona.objects.none()

class ProductoList(ListView):
    model = Producto
    #template_name = 'producto_list.html'

class ProductoDetail(DetailView):
    model = Producto
    #template_name = 'producto_detail.html'

class ProductoCreate(CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'descripcion']
    #template_name = 'producto_form.html'
    success_url = reverse_lazy('producto-llist')

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'descripcion']
    #template_name = 'producto_form.html'
    success_url = reverse_lazy('producto-list')

class ProductoDelete(DeleteView):
    model = Producto
    #template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')

def mostrar_productos(request):
    
    productos = Producto.objects.all()
    total_productos = len(productos)
    context = {
        "productos": productos, 
        "total_productos":total_productos,
        "form": ProductoForm(),
    }
    return render(request, "Entrega3/producto.html", context)

def crear_prductos(request):

    f = ProductoForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Producto(nombre=f.data["nombre"], descripcion=f.data["descripcion"], precio=f.data["precio"]).save()
        context['form'] = ProductoForm()

    context["productos"] = Producto.objects.all()
    context["total_productos"] = len(Producto.objects.all())
         
    return render(request, "Entrega3/productos.html", context)

class BuscarProductos(ListView):
    model = Producto
    context_object_name = "productos"

    def get_queryset(self):
        f = BuscarProductosForm(self.request.GET)
        if f.is_valid():
           return Producto.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Producto.objects.none()