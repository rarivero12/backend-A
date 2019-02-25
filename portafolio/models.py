from django.db import models
from django.contrib.auth.models import User



#Pruebas
class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("poll", "voted_by")



##########  Modelos de aplicacion portafolio #######################
class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)
    telefono = models.CharField(max_length=20)
    pagina = models.CharField(max_length=20,default='Inicio')
    def __str__(self):
        return self.nombre + " " + self.apellido

class Imagen(models.Model):
    titulo = models.CharField(max_length=40)
    numero_imagen = models.IntegerField()
    imagen = models.ImageField(blank=True)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titulo

class Archivo(models.Model):
    titulo = models.CharField(max_length=40)
    numero_archivo = models.IntegerField()
    archivo = models.FileField(blank=True)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titulo


#####################  POST ############################################
class Categoria_post(models.Model):
    nombre_categoria = models.CharField(max_length=20)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre_categoria


class Post(models.Model):
    titulo = models.CharField(max_length=40)
    sub_titulo = models.CharField(max_length=40)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria_post, on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen)
    def __str__(self):
        return self.titulo


class TextoPost(models.Model):
    titulo_texto = models.CharField(max_length=40)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='textos', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo_texto


################ PORTAFOLIO ###################################

class CategoriaPortafolio(models.Model):
    nombre_categoria = models.CharField(max_length=20)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre_categoria

class Colaborador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    red_social = models.CharField(max_length=50)
    pagina_web = models.URLField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre + self.apellido

class Portafolio(models.Model):
    titulo_proyecto = models.CharField(max_length=40)
    titulo_inferior = models.CharField(max_length=40)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(CategoriaPortafolio, on_delete=models.CASCADE)
    colaboradores = models.ManyToManyField(Colaborador)
    imagenes = models.ManyToManyField(Imagen)
    def __str__(self):
        return self.titulo_proyecto


############### Servicios ###############################33

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=20)
    vigencia = models.IntegerField(default=1)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    costo = models.CharField(max_length=40)
    modalidad = models.CharField(max_length=40)
    lugar = models.CharField(max_length=40)
    horario = models.CharField(max_length=40)
    vigencia = models.IntegerField(default=1)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    tipo_servicio = models.ForeignKey(TipoServicio,related_name='servicios', on_delete=models.CASCADE)
    flayer = models.ForeignKey(Imagen, on_delete=models.CASCADE)
    archivos = models.ManyToManyField(Archivo)
    def __str__(self):
        return self.nombre

class IncluyeServicio(models.Model):
    descripcion = models.CharField(max_length=60)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    servicio = models.ForeignKey(Servicio, related_name='Incluye_servicio', on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.descripcion

class ContenidoServicio(models.Model):
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)
    servicio = models.ForeignKey(Servicio, related_name='contenido_servicio', on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.titulo

class ProductosServicio(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    servicio = models.ForeignKey(Servicio, related_name='productos_servicio', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class RequisitosServicio(models.Model):
    requisito = models.CharField(max_length=60)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    servicio = models.ForeignKey(Servicio, related_name='requisitos_servicio', on_delete=models.CASCADE)
    def __str__(self):
        return self.requisito
