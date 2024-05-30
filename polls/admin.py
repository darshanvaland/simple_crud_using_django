from django.contrib import admin
from .models import crate
# Register your models here.
class ragistercreate(admin.ModelAdmin):
    list_display = ('name','mobile','email','birth')
    fields=('name','mobile','email','birth')

admin.site.register(crate,ragistercreate)