from django.contrib import admin
from .models import *

# Registadmin.site.register(Product,ProductAdmin)
admin.site.register(Vaga)
admin.site.register(Cidade)
admin.site.register(Empresa)
admin.site.register(TipoVaga)
