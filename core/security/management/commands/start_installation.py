import os

import django
from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('++++++++++++++++++++++++ INGRESANDO DATA BASE DEL PROYECTO ++++++++++++++++++++++++ ')
        print("")
        print("++++++++++++++++++++++++ CREANDO GRUPOS (ROLES) ++++++++++++++++++++++++")
        print("")
        group_administrador = Group.objects.create(name='Administrador')
        print(f'Insertando {group_administrador.name}')
        group_empleado = group = Group.objects.create(name='Empleado')
        print(f'Insertando {group_empleado.name}')
        # print("++++++++++++++++++++++++ VINCULANDO USUARIO CON GRUPOS (ROLES) ++++++++++++++++++++++++")
        # print("")
        print("++++++++++++++++++++++++ AGREGANDO PERMISOS ++++++++++++++++++++++++")
        print("")
        permissions_employee_admin = Permission.objects.filter(codename__contains='employee')
        group_administrador.permissions.add(*permissions_employee_admin)
        print(f'Agregando permisos a {group_administrador.name}')
        permission_view_employee = Permission.objects.filter(codename='view_employee')
        group_empleado.permissions.add(*permission_view_employee)
        print(f'Agregando permisos a {group_empleado.name}')
        print("++++++++++++++++++++++++ CREANDO USUARIO ADMINISTRADOR ++++++++++++++++++++++++")
        user_admin = User.objects.create(
            first_name='Esteban',
            last_name='Vizhnay',
            username='admin',
            email='admin@test.com',
            is_active=True,
            is_superuser=True,
            is_staff=True
        )
        user_admin.set_password('admin95')
        user_admin.save()
        user_admin.groups.add(group_administrador)
        print(f'Bienvenido {user_admin.first_name} {user_admin.last_name}')
        print("++++++++++++++++++++++++ CREANDO USUARIO EMPLEADO ++++++++++++++++++++++++")
        user_employee = User.objects.create(
            first_name='Pepe',
            last_name='Perez',
            username='pperez',
            email='empleado@test.com',
            is_active=True,
        )
        user_employee.set_password('empleado95')
        user_employee.save()
        user_employee.groups.add(group_empleado)
        print(f'Bienvenido {user_employee.first_name} {user_employee.last_name}')
