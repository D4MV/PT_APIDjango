from rest_framework import serializers
from .models import Producto

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'fecha', 'valor', 'imagen')
        read_only_fields = ('id', 'fecha', )

