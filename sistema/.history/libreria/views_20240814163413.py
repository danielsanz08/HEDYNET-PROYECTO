from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Transaccion, Insumo
from django.contrib.auth.decorators import login_required
from .forms import InsumoForm, UsuarioForm
from django.contrib import messages
from .forms import SignUpForm
@login_required
def inicio(request):
    return render(request, 'index/index.html')

@login_required
def usuario(request):
    return render(request, 'usuario/usuario.html')

@login_required
def contabilidad(request):
    return render(request, 'paginas/finanza.html')

@login_required
def insumos(request):
    return render(request, 'insumos/insumos.html')

@login_required
def ver_perfil(request):
    return render(request, 'usuario/ver.html')

@login_required
def editar_perfil(request):
    return render(request, 'usuario/editar.html')

@login_required
def cambiar_contraseña(request):
    return render(request, 'usuario/nueva_contraseña.html')

def login(request):
    return render(request, 'login/login.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            
            if password1 != password2:
                messages.error(request, 'Las contraseñas no coinciden.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Usuario registrado exitosamente.')
                return redirect('login')  # Asegúrate de que 'login' sea el nombre correcto
        else:
            messages.error(request, 'Formulario inválido. Corrija los errores.')
    else:
        form = SignUpForm()
    return render(request, 'registro.html', {'form': form})
@login_required
def ver_transacciones(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'transacciones/ver.html', {'transacciones': transacciones})

@login_required
def crear_transacciones(request):
    if request.method == 'POST':
        tipo = request.POST['tipo']
        descripcion = request.POST['descripcion']
        monto = request.POST['monto']
        fecha = request.POST['fecha']
        
        transaccion = Transaccion(tipo=tipo, descripcion=descripcion, monto=monto, fecha=fecha)
        transaccion.save()
        
        return redirect('ver_transacciones')

    return render(request, 'transacciones/crear.html')

@login_required
def eliminar(request, id):
    transaccion = Transaccion.objects.get(id=id)
    transaccion.delete()
    return redirect('ver_transacciones')

@login_required
def search(request):
    search_type = request.GET.get('type')
    query = request.GET.get('query')

    if search_type == 'fecha':
        transacciones = Transaccion.objects.filter(fecha__icontains=query)
    elif search_type == 'descripcion':
        transacciones = Transaccion.objects.filter(descripcion__icontains=query)
    else:
        transacciones = Transaccion.objects.all()

    results = list(transacciones.values('tipo', 'descripcion', 'monto', 'fecha'))
    return JsonResponse(results, safe=False)

@login_required
def listar_usuario(request):
    return render(request, 'usuario/listar.html')

@login_required
def agregar_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultar_insumo')
    else:
        form = InsumoForm()
    return render(request, 'insumos/agregar_insumo.html', {'form': form})

@login_required
def editar_insumo(request):
    insumos = Insumo.objects.all()
    form = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        insumo = Insumo.objects.filter(nombre=nombre).first()

        if insumo:
            form = InsumoForm(request.POST, instance=insumo)
            if form.is_valid():
                form.save()
                return redirect('consultar_insumo')
        else:
            return render(request, 'insumos/editar_insumo.html', {'insumos': insumos})
    else:
        nombre = request.GET.get('nombre')
        if nombre:
            insumo = Insumo.objects.filter(nombre=nombre).first()
            if insumo:
                form = InsumoForm(instance=insumo)
            else:
                return render(request, 'insumos/editar_insumo.html', {'insumos': insumos})
    return render(request, 'insumos/editar_insumo.html', {'form': form, 'insumos': insumos})

@login_required
def eliminar_insumo(request, id):
    insumo = Insumo.objects.get(id=id)
    insumo.delete()
    return redirect('consultar_insumo')

@login_required
def consultar_insumo(request):
    query = request.GET.get('q', '')
    if query:
        insumos = Insumo.objects.filter(nombre__icontains=query)
    else:
        insumos = Insumo.objects.all()
    return render(request, 'insumos/consultar_insumo.html', {'insumos': insumos})