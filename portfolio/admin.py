from django.contrib import admin

from .models import Script
# Register your models here.

class ScriptAdmin(admin.ModelAdmin):
    pass
admin.site.register(Script, ScriptAdmin)