from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
=======
from django.contrib.auth.models import User

>>>>>>> ceb4bc462374777be02770693ad54b35882e81f4


class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, password=None, **extra_fields):
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        if not password:
            raise ValueError('El usuario debe tener una contraseña')
        
        user = self.model(nombre=nombre, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nombre, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    rol = models.CharField(max_length=100, choices=[('Administrador', 'Administrador'), ('Empleado', 'Empleado')], default='Empleado')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nombre'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nombre
    
class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('Compra', 'Compra'),
        ('Venta', 'Venta'),
        ('Gasto', 'Gasto'),
        ('Ingreso', 'Ingreso'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    monto = models.DecimalField(max_digits=10, decimal_places=3, default=100.00, verbose_name="Monto")
    fecha = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.descripcion} - ${self.monto}"

class Insumo(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="nombre")
    descripcion = models.TextField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    ROL_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Empleado', 'Empleado'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True)
    nombre = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    telefono = models.CharField(max_length=15, null=True)
    contraseña = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user

