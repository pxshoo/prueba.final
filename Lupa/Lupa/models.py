from django.db import models

class usuario(models.Model):
    nomUsuario = models.CharField(max_length=255,unique=True)
    correo = models.EmailField(max_length=255,unique=True)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.nomUsuario


