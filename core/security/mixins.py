from django.contrib.auth.models import Group, Permission
from rest_framework import permissions, exceptions


class IsInGroupPermission(permissions.BasePermission):
    """
    Custom permission to check if the user is in a required group.
    """

    def __init__(self, permission_required):
        self.permission_required = permission_required

    def has_permission(self, request, view):

        print(f"Usuario: {request.user}")
        # obtenemos los grupos del usuario
        grupos_usuario = request.user.groups.all()
        print(f"Grupo del usuario: {grupos_usuario}")

        # permisos del usuario de acuerdo a sus grupos
        permisos_grupos_usuario = []
        for grupo in grupos_usuario:
            # Obtener todos los permisos asignados a este grupo
            permisos_grupo = grupo.permissions.all()
            for permiso in permisos_grupo:
                permisos_grupos_usuario.append(permiso.codename)
        # print(request.user)
        print(f"Permisos del grupo del usuario: {permisos_grupos_usuario}")
        print(f"Permiso requerido: {self.permission_required}")
        if self.permission_required in permisos_grupos_usuario:
            print('Validacion exitosa')
            return True
        raise exceptions.PermissionDenied({'mensaje': "No tienes permisos para realizar la petición"})
