from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.
def inicio_vistaVentas(request):
    lasventas = Ventas.objects.all()
    return render(request, "gestionarVentas.html", {"misventas": lasventas})

def registrarVenta(request):
    id_venta = request.POST["txtcodigo"]
    id_cliente = request.POST["txtcliente"]
    id_trabajador = request.POST["txttrabajador"]
    id_troca = request.POST["txttroca"]
    cantidad = request.POST["txtcantidad"]
    fecha_venta = request.POST["txtfecha"]
    total = request.POST["txttotal"]

    Ventas.objects.create(
        id_venta=id_venta,
        id_cliente=id_cliente,
        id_trabajador=id_trabajador,
        id_troca=id_troca,
        cantidad=cantidad,
        fecha_venta=fecha_venta,
        total=total,
    )  # GUARDA EL REGISTRO

    return redirect("ventas")

def seleccionarVenta(request, codigo):
    venta = Ventas.objects.get(id_venta=codigo)
    fecha_venta = venta.fecha_venta.strftime('%Y-%m-%d')
    return render(request, "editarVentas.html", {"misventas": venta, "misventas": venta, "fecha_venta": fecha_venta})

def editarVenta(request):
    id_venta = request.POST["txtcodigo"]
    id_cliente = request.POST["txtcliente"]
    id_trabajador = request.POST["txttrabajador"]
    id_troca = request.POST["txttroca"]
    cantidad = request.POST["txtcantidad"]
    fecha_venta = request.POST["txtfecha"]
    total = request.POST["txttotal"]

    venta = Ventas.objects.get(id_venta=id_venta)
    venta.id_cliente = id_cliente
    venta.id_trabajador = id_trabajador
    venta.id_troca = id_troca
    venta.cantidad = cantidad
    venta.fecha_venta = fecha_venta
    venta.total = total
    venta.save()  # GUARDA EL REGISTRO ACTUALIZADO

    return redirect("ventas")

def borrarVenta(request, codigo):
    venta = Ventas.objects.get(id_venta=codigo)
    venta.delete()  # BORRA EL REGISTRO
    return redirect("ventas")
