from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title = ''
admin.site.site_header = 'Financ'

admin.site.register(Uf)
admin.site.register(Muncipio)
admin.site.register(Empresa)
