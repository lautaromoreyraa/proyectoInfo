from django.contrib import admin
from .models import Noticia
# Register your models here.

class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha", )

admin.site.register(Noticia, NoticiasAdmin)
