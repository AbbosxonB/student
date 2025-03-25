from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Yunalish)
class YunalishAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']



@admin.register(Kursi)
class KursiAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
@admin.register(Shakli)
class ShakliAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
@admin.register(Turi)
class TuriAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('question', 'get_subjects', 'correct')
    search_fields = ('question',)
    list_filter = ('fan',)

    def get_subjects(self, obj):
        return ", ".join([fan.name for fan in obj.fan.all()])
    
    get_subjects.short_description = "Fanlar"  # Admin panel ustuni nomi