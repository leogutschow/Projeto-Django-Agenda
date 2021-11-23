from django.contrib import admin
from .models import Categoria, Contato
# Register your models here.

class ContatosAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'sobrenome', 'email',
        'mostrar'
    )
    
    list_display_links = (
        'id', 'nome'
    )
    
    list_editable = (
        'email','mostrar'
    )

admin.site.register(Contato, ContatosAdmin)
admin.site.register(Categoria)