from django.db import models


# Create your models here.
class Employee(models.Model):
    dni = models.CharField(max_length=15, unique=True, verbose_name='dni')  # obligatorio
    first_name = models.CharField(max_length=150, verbose_name='nombre')  # obligatorio
    last_name = models.CharField(max_length=150, verbose_name='apellido')  # obligatorio
    email = models.EmailField(unique=True, verbose_name='email')  # obligatorio
    position = models.CharField(max_length=100, verbose_name='posicion')  # obligatorio
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='telefono')
    address = models.CharField(max_length=2000, null=True, blank=True, verbose_name='direccion')

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    '''
    Id, FirstName, LastName, Email,
    Position, phone, address, id.'''
