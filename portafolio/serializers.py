from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group



#Pruebas de serializers
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



#Serializer de aplicacion portafolio
class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = '__all__'


############3Portafolio serializers ###############################


class CategoriaPortafolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPortafolio
        fields = '__all__'

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'

class PortafolioSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(read_only=True, many=True)
    colaboradores = ColaboradorSerializer(read_only=True, many=True)
    categoria = CategoriaPortafolioSerializer(read_only=True)

    class Meta:
        model = Portafolio
        fields = '__all__'


############# SERVICIOS #################

class TipoServicioSerializer(serializers.ModelSerializer):
    servicios = serializers.StringRelatedField(many=True)
    class Meta:
        model = TipoServicio
        fields = '__all__'

class IncluyeServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncluyeServicio
        fields = '__all__'

class ContenidoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenidoServicio
        fields = '__all__'

class ProductosServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosServicio
        fields = '__all__'

class RequisitosServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitosServicio
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    flayer = ImagenSerializer(read_only=True)
    archivos = ArchivoSerializer(read_only=True, many=True)
    tipo_servicio = TipoServicioSerializer(read_only=True)
    Incluye_servicio = serializers.StringRelatedField(many=True)
    contenido_servicio = serializers.StringRelatedField(many=True)
    productos_servicio = serializers.StringRelatedField(many=True)
    requisitos_servicio = serializers.StringRelatedField(many=True)

    class Meta:
        model = Servicio
        fields = '__all__'
