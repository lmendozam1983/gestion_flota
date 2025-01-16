from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, VehiculoForm, AsignacionForm, SignInForm
from django.contrib import messages
from .models import Vehiculo, Asignacion

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm  # Ajusta esto según el nombre real de tu formulario

def usuario_nuevo(request):
    if request.method == "POST":
        form = UserForm(request.POST)  # Ajusta el nombre del formulario
        if form.is_valid():
            # Guardar el nuevo usuario
            form.save()
            messages.success(request, "Usuario creado exitosamente.")
            return redirect('/')  # Cambia por la URL o vista correspondiente
        else:
            messages.error(request, "Error al crear el usuario. Revisa los datos proporcionados.")
            # Renderiza nuevamente el formulario con errores
            return render(request, 'usuario_nuevo.html', {'form': form})

    # Si es un GET o cualquier otro método, muestra un formulario vacío
    form = UserForm()
    return render(request, 'usuario_nuevo.html', {'form': form})

    
def usuarios_lista(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios_lista.html', {'usuarios': usuarios})

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Loguear al usuario
                login(request, user)  # Aquí pasamos correctamente `request` y `user`
                return redirect('flota/usuarios')  # Redirige a la página principal o a donde prefieras
            else:
                form.add_error(None, "Usuario o contraseña incorrectos")
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})

def logout_view(request):
    logout(request) 
    messages.success(request, "Has cerrado sesión correctamente.") 
    return redirect('login')  
    
def vehiculo_lista(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo_lista.html', {'vehiculos': vehiculos})

def vehiculo_nuevo(request):
    form = VehiculoForm()
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculos')
    else:
        form = VehiculoForm()
        return render(request, 'vehiculo_nuevo.html', {'form': form})
    
def vehiculo_editar(request,id):
    vehiculo = Vehiculo.objects.get(id=id)
    form = VehiculoForm(instance=vehiculo)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
        return render(request, 'vehiculo_editar.html', {'form': form})
    
def vehiculo_eliminar(request,id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    return redirect('vehiculos')
    
def asignacion_lista(request):
    if request.user.has_perm('flota.view_asignacion'):
        # Usuario con permiso para ver todas las asignaciones
        asignaciones = Asignacion.objects.all()
    else:
        # Usuario con permiso para ver solo sus asignaciones
        asignaciones = Asignacion.objects.filter(usuario=request.user)
    context = {'asignaciones':asignaciones}
    return render(request,'asignacion_lista.html',context)

def asignacion_nueva(request):
    form = AsignacionForm()
    if request.method == 'POST':
        form = AsignacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asignaciones')
    else:
        form = AsignacionForm()
        return render(request, 'asignaciones_nueva.html', {'form': form})
    
def asignaciones_editar(request,id):
    asignacion = Asignacion.objects.get(id=id)
    form = AsignacionForm(instance=asignacion)
    if request.method == 'POST':
        form = AsignacionForm(request.POST, instance=asignacion)
        if form.is_valid():
            form.save()
            return redirect('asignaciones')
    else:
        form = AsignacionForm(instance=asignacion)
        return render(request, 'asignaciones_editar.html', {'form': form})
    
def asignaciones_eliminar(request,id):
    asignacion = Asignacion.objects.get(id=id)
    asignacion.delete()
    return redirect('asignaciones')