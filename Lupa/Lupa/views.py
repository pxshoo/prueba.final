from django.shortcuts import render,redirect
from .models import usuario  

def login_view(request):
       return render(request, 'paginas/login.html')

def prueba_view(request):
    return render(request, 'paginas/prueba.html')

def Nosotros_view(request):
    return render(request, 'paginas/Nosotros.html')

def Register_view(request):

    if request.method == 'POST':
        # Procesar el formulario cuando se envíe por POST
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validar que las contraseñas coincidan
        if password != confirm_password:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'paginas/Register.html', {'error_message': error_message})

        # Crear una instancia del modelo usuario y guardarla en la base de datos
        nuevo_usuario = usuario(nomUsuario=username, correo=email, contraseña=password)
        nuevo_usuario.save()

        return redirect("{% url 'login.' %}")  
    else:
        return render(request, 'paginas/Register.html')
