# En archivo myapp/admin.py
from django.contrib import admin
from .models import Usuario

# Registra el modelo Usuario para que sea visible en el admin de Django
admin.site.register(Usuario)
