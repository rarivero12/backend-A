from django.contrib import admin

# Register your models here.
from .models import *


#############  CLASES PARA TODOS ##############################

class ColaboradorAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('nombre', 'apellido')
    search_fields = ['nombre', 'apellido']
    list_filter = ['fecha_publicacion']

admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Imagen)
admin.site.register(Archivo)

##### CODIGO PARA VISTAS DE SITIO ADMINISTRATIVO POST @#####
class TextoInline(admin.TabularInline):
    model = TextoPost
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = Post

    fieldsets = [
        ('CATEGORIA', {'fields': ['categoria']}),
        ('INFORMACION BASICA', {'fields': ['titulo','sub_titulo']}),
        ('IMAGENES', {'fields': ['imagenes']}),
    ]
    inlines = [TextoInline]
    list_display = ('titulo', 'fecha_publicacion')
    search_fields = ['titulo']
    list_filter = ['fecha_publicacion']



admin.site.register(Post, PostAdmin)
admin.site.register(Categoria_post)


###### ADMINISTRATIVO CONTACTOS #####################

class ContactoAdmin(admin.ModelAdmin):
    model = Contacto
    list_display = ('nombre', 'apellido','fecha_publicacion' ,'pagina')
    search_fields = ['nombre','apellido','pagina']
    list_filter = ['fecha_publicacion', 'pagina']


admin.site.register(Contacto, ContactoAdmin)

######### ADMINISTRATIVO PARA PORTAFOLIO ##################


class PortafolioAdmin(admin.ModelAdmin):
    model = Portafolio

    fieldsets = [
        ('CATEGORIA', {'fields': ['categoria']}),
        ('INFORMACION PORTAFOLIO', {'fields': ['titulo_proyecto','titulo_inferior','descripcion','colaboradores']}),
        ('IMAGENES', {'fields': ['imagenes']}),
    ]
    list_display = ('titulo_proyecto', 'fecha_publicacion')
    search_fields = ['titulo_proyecto','titulo_inferior']
    list_filter = ['fecha_publicacion','colaboradores']



admin.site.register(Portafolio, PortafolioAdmin)
admin.site.register(CategoriaPortafolio)


############################################################




class ServicioAdmin(admin.ModelAdmin):
    model = Servicio

    fieldsets = [
        ('TIPO', {'fields': ['tipo_servicio']}),
        ('INFORMACION BASICA', {'fields': ['nombre','descripcion','costo','modalidad','lugar','horario','vigencia']}),
        ('FLAYER', {'fields': ['flayer']}),
        ('ARCHIVOS', {'fields': ['archivos']}),
    ]
    list_display = ('nombre', 'tipo_servicio', 'fecha_publicacion')
    search_fields = ['nombre']
    list_filter = ['fecha_publicacion','tipo_servicio']



admin.site.register(Servicio, ServicioAdmin)
admin.site.register(TipoServicio)
