from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings



#Vistas de aplicacion portafolio
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

    @action(detail=False,  methods=['post','get'])
    def escribir(self, request,pk=None):
        subject = 'Thank you for registering to our site'
        print(request.data)
        message = request.data['nombre'] 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rafaelarturo16@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        return Response({'status': 'Correo enviadoS'})




class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

#Portafolio
class CategoriaPortafolioViewSet(viewsets.ModelViewSet):
    queryset = CategoriaPortafolio.objects.all()
    serializer_class = CategoriaPortafolioSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

class PortafolioViewSet(viewsets.ModelViewSet):
    queryset = Portafolio.objects.all()
    serializer_class = PortafolioSerializer


######### Servicios ##############33333

class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer

class IncluyeServicioViewSet(viewsets.ModelViewSet):
    queryset = IncluyeServicio.objects.all()
    serializer_class = IncluyeServicioSerializer

class ContenidoServicioViewSet(viewsets.ModelViewSet):
    queryset = ContenidoServicio.objects.all()
    serializer_class = ContenidoServicioSerializer

class ProductosServicioViewSet(viewsets.ModelViewSet):
    queryset = ProductosServicio.objects.all()
    serializer_class = ProductosServicioSerializer

class RequisitosServicioViewSet(viewsets.ModelViewSet):
    queryset = RequisitosServicio.objects.all()
    serializer_class = RequisitosServicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


#Pruebas
class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer


class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
