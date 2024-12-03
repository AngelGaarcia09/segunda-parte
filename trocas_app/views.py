from django.shortcuts import render, redirect
from .models import Troca

# Create your views here.
def inicio_vistaTrocas(request):
    lastrocas = Troca.objects.all()
    return render(request, "gestionarTrocas.html", {"mistrocas": lastrocas})

def registrarTroca(request):
    id_troca = request.POST["txtcodigo"]
    año = request.POST["txtanio"]
    modelo = request.POST["txtmodelo"]
    marca = request.POST["txtmarca"]
    precio = request.POST["txtprecio"]
    date = request.POST["txtfecha"]
    tipo_llantas = request.POST["txtllantas"]

    Troca.objects.create(
        id_troca=id_troca,
        año=año,
        modelo=modelo,
        marca=marca,
        precio=precio,
        date=date,
        tipo_llantas=tipo_llantas,
    )  # Guarda el registro

    return redirect("trocas")

def seleccionarTroca(request, codigo):
    troca = Troca.objects.get(id_troca=codigo)
    date = troca.date.strftime('%Y-%m-%d')
    return render(request, "editarTroca.html", {"mistrocas": troca, "mistrocas": troca, "date": date})

def editarTroca(request):
    id_troca = request.POST["txtcodigo"]
    año = request.POST["txtanio"]
    modelo = request.POST["txtmodelo"]
    marca = request.POST["txtmarca"]
    precio = request.POST["txtprecio"]
    date = request.POST["txtfecha"]
    tipo_llantas = request.POST["txtllantas"]

    troca = Troca.objects.get(id_troca=id_troca)
    troca.año = año
    troca.modelo = modelo
    troca.marca = marca
    troca.precio = precio
    troca.date = date
    troca.tipo_llantas = tipo_llantas
    troca.save()  # Guarda el registro actualizado

    return redirect("trocas")

def borrarTroca(request, codigo):
    troca = Troca.objects.get(id_troca=codigo)
    troca.delete()  # Borra el registro
    return redirect("trocas")
