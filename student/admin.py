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

@admin.register(Guruh)
class GuruhAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'yunalish_display', 'kursi_display')
    list_filter = ('name', 'yunalish', 'kursi')

    def yunalish_display(self, obj):
        return ", ".join([y.name for y in obj.yunalish.all()])
    
    yunalish_display.short_description = "Yunalishlar"

    def kursi_display(self, obj):
        return obj.kursi.name if obj.kursi else "Mavjud emas"
    
    kursi_display.short_description = "Kurs"


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('question', 'get_subjects', 'correct')
    search_fields = ('question',)
    list_filter = ('fan',)

    def get_subjects(self, obj):
        return ", ".join([fan.name for fan in obj.fan.all()])
    
    get_subjects.short_description = "Fanlar"  # Admin panel ustuni nomi