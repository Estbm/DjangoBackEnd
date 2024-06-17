from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response

from core.manager.models import Employee
from core.manager.apis.serializers import EmployeeSerializer
from core.security.mixins import IsInGroupPermission


#  listar y crear empleados
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def employees_api_view(request):
    # listar empleados
    if request.method == 'GET':
        permission_required = 'view_employee'
        # validacion de permisos
        permission = IsInGroupPermission(permission_required)
        permission.has_permission(request, None)
        # obtenemos todos los empleados
        employees = Employee.objects.all()
        # serializamos lo obtenido
        employess_serializer = EmployeeSerializer(employees, many=True)
        return Response({
            'mensaje': 'Empleados obtenidos exitosamente',
            'resultado': employess_serializer.data
        }, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        permission_required = 'add_employee'
        # validacion de permisos
        permission = IsInGroupPermission(permission_required)
        permission.has_permission(request, None)
        # serializamos el request enviado
        employee_serializer = EmployeeSerializer(data=request.data)
        # validamos la serializacion
        if employee_serializer.is_valid():
            # guardamos
            employee_serializer.save()
            return Response({
                'mensaje': 'Empleado creado exitosamente',
                'resultado': employee_serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'mensaje': 'Error al crear el empleado',
            'errores': employee_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def employee_detail_api_view(request, pk=None):
    # existe un empleado con el id enviado
    employee = Employee.objects.filter(pk=pk).first()

    if employee is not None:

        if request.method == 'GET':
            permission_required = 'view_employee'
            # validacion de permisos
            permission = IsInGroupPermission(permission_required)
            permission.has_permission(request, None)
            # serializamos al empleado
            employee_serializer = EmployeeSerializer(employee)
            return Response({'mensaje': 'Empleado obtenido exitosamente', 'resultado': employee_serializer.data},
                            status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            permission_required = 'change_employee'
            # validacion de permisos
            permission = IsInGroupPermission(permission_required)
            permission.has_permission(request, None)
            # serializamos al empleado
            employee_serializer = EmployeeSerializer(employee, data=request.data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return Response({'mensaje': 'Empleado actualizado exitosamente', 'resultado': employee_serializer.data},
                                status=status.HTTP_200_OK)
            return Response({
                'mensaje': 'Error al actualizar el empleado',
                'errores': employee_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            permission_required = 'delete_employee'
            # validacion de permisos
            permission = IsInGroupPermission(permission_required)
            permission.has_permission(request, None)
            # eliminamos el empleado
            employee.delete()
            return Response({'mensaje': 'Empleado eliminado exitosamente'}, status=status.HTTP_200_OK)

    return Response({'mensaje': 'No se ha encontrado el empleado con el id enviado'},
                    status=status.HTTP_400_BAD_REQUEST)
