from django.db import models


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

    def _str_(self):
        return self.nombre
    
class Usuario(models.Model):
    ROL_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Empleado', 'Empleado'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True)
    nombre = models.CharField(max_length=100, null=True)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    
    email = models.EmailField(max_length=254, null=True)
    contraseña = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user

