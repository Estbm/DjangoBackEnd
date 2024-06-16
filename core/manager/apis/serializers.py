from rest_framework import serializers

from core.manager.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(required=True)
    # dni = serializers.CharField(max_length=15, required=True)

    class Meta:
        model = Employee
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     validated_data.pop('dni', None)
    #     return super().update(instance, validated_data)
    #
    # def validate_email(self, value):
    #     if Employee.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("El correo ya se encuentra registrado.")
    #     return value
    #
    # def validate_dni(self, value):
    #     if Employee.objects.filter(dni=value).exists():
    #         raise serializers.ValidationError("La identificación se encuentra registrado.")
    #     return value
