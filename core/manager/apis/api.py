from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.manager.models import Employee
from core.manager.apis.serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404


# prueba de api
@api_view(['GET'])
def test(request):
    return Response({'mensaje': 'ok'})


#  listar y crear empleados
@api_view(['GET', 'POST'])
def employees_api_view(request):
    # listar empleados
    if request.method == 'GET':
        # obtenemos todos los empleados
        employees = Employee.objects.all()
        # serializamos lo obtenido
        employess_serializer = EmployeeSerializer(employees, many=True)
        return Response({
            'mensaje': 'Empleados obtenidos exitosamente',
            'resultado': employess_serializer.data
        }, status=status.HTTP_200_OK)
    elif request.method == 'POST':
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
def employee_detail_api_view(request, pk=None):
    # existe un empleado con el id enviado
    employee = Employee.objects.filter(pk=pk).first()

    if employee is not None:

        if request.method == 'GET':
            # serializamos al empleado
            employee_serializer = EmployeeSerializer(employee)
            return Response({'mensaje': 'Empleado obtenido exitosamente', 'resultado': employee_serializer.data},
                            status=status.HTTP_200_OK)

        elif request.method == 'PUT':
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
            # eliminamos el empleado
            employee.delete()
            return Response({'mensaje': 'Empleado eliminado exitosamente'}, status=status.HTTP_200_OK)

    return Response({'mensaje': 'No se ha encontrado el empleado con el id enviado'},
                    status=status.HTTP_400_BAD_REQUEST)
