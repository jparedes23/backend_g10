from django.contrib.auth.models import BaseUserManager

## BaseUserManager > sirve para modificar la creacion y administracion de los auth_user

class UsuarioManager(BaseUserManager):
    ## esta clase me permitira modificar la administracion del usuario mediante el comando createsuperuser
    def create_superuser(self, correo, nombre, apellido, tipoUsuario, password):
        # valido si no hya correo
        if not correo:
            raise ValueError("el usuario no proporciono el correo")
        # valido que el correo cumpla con el formato correcto
        # removera los espacio al inicio y al final y validara que no utilice caracteres incorrectos
        correo_normalizado = self.normalize_email(correo)
        ## llamamos al modelo que estamos utilizando e inicializamos el nuevo usuario
    ## self.model -> es el modelo usuario
        nuevo_usuario = self.model(correo= correo_normalizado, nombre = nombre, apellido = apellido, tipoUsuario= tipoUsuario)

    ## generamos el hash de la contraseña
    ## generar  el hash de la contraseña utilizando algoritmos de hash sha512
        nuevo_usuario.set_password(password) #> genera el hash de la contraseña

        nuevo_usuario.is_superuser = True # para indicar que es super usuario
        nuevo_usuario.is_staff = True# para indicar si pertenece al grupo de trabjo
        nuevo_usuario.save()