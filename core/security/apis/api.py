

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.security.apis.serializers import UserSerializer


@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    # la informacion es valida
    if serializer.is_valid():
        # guardamos el usuario a crear
        serializer.save()
        # # creamos un token
        # token = Token.objects.create(user=user)
        return Response({'mensaje': 'Registrado', 'resultado': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# api de prueba
@api_view(['GET'])
def test(request):
    return Response({'mensaje': 'ok'})


# api de prueba token
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({'mensaje': 'prueba de token exitosa!!!'})
