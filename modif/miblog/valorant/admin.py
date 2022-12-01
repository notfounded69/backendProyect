from django.contrib import admin


from .models import Categoria, Agentes

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Agentes)
# Register your models here.
