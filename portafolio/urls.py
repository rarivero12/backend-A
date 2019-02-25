from django.urls import path
from .restviews import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


app_name = 'portafolio'


#Rutas predeterminadas de django rest
router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
router.register('contacto', ContactoViewSet, base_name='contacto')
router.register('imagen', ImagenViewSet, base_name='imagen')
router.register('archivo', ArchivoViewSet, base_name='archivo')

router.register('categoriaport', CategoriaPortafolioViewSet, base_name='categoriaport')
router.register('colaborador', ColaboradorViewSet, base_name='colaborador')
router.register('portafolio', PortafolioViewSet, base_name='portafolio')
router.register('tipoServicio',TipoServicioViewSet,base_name='tipo_servicio')

# Servicios


router.register('servicio', ServicioViewSet, base_name='servicio')


#rutas por mi
urlpatterns = [
    path("pol/", PollList.as_view(), name="polls_list"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("users/", UserViewSet.as_view(), name="user_list"),
    path("groups/", GroupViewSet.as_view(), name="group_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("vote/", CreateVote.as_view(), name="create_vote"),

]


urlpatterns += router.urls

#Para poder ver las imagnes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
