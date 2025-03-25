from django.contrib import admin
from .models import *
from .formats import *
from .resources import YourModelResource
from django import forms

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



from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import YourModel  # Modelingizni import qiling

# Excel yuklash uchun resurs yaratish
class YourModelResource(resources.ModelResource):
    class Meta:
        model = YourModel

from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import XLS, XLSX

class YourModelAdmin(ImportExportModelAdmin):
    resource_class = YourModelResource

    def get_import_formats(self):
        """ Import qilish uchun qo‘shimcha formatlarni qaytaradi """
        formats = super().get_import_formats()
        formats.extend([XLS(), XLSX()])
        return formats

    def get_export_formats(self):
        """ Export qilish uchun qo‘shimcha formatlarni qaytaradi """
        formats = super().get_export_formats()
        formats.extend([XLS(), XLSX()])
        return formats

from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import XLS, XLSX
from .resources import YourModelResource

# ✅ Admin panelga qo‘shimcha forma - foydalanuvchidan fan tanlash
class YourModelImportForm(forms.Form):
    fan = forms.ModelChoiceField(queryset=Fan.objects.all(), required=True, label="Fan tanlang")

@admin.register(YourModel)
class YourModelAdmin(ImportExportModelAdmin):
    resource_class = YourModelResource

    def get_export_formats(self):
        formats = super().get_export_formats()  # Default formatlarni olamiz
        return [XLS(), XLSX()] + formats  # Excel formatlarini qo'shamiz

    def get_import_form(self):
        return YourModelImportForm

    def get_import_data_kwargs(self, request, *args, **kwargs):
        selected_fan_id = request.POST.get("fan")
        kwargs = super().get_import_data_kwargs(request, *args, **kwargs)
        kwargs.update({"user_selected_fan_id": selected_fan_id})
        return kwargs


class YourModelImportForm(forms.Form):
    fan = forms.ModelChoiceField(queryset=Fan.objects.all(), required=True, label="Fan tanlang")