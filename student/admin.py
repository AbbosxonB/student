import pandas as pd
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect


from .models import *

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

# 📌 Excel yuklash uchun form
class ExcelImportForm(forms.Form):
    fan = forms.ModelChoiceField(queryset=Fan.objects.all(), label="Fan tanlang")
    excel_file = forms.FileField(label="Excel faylni yuklang")


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('question', 'get_subjects', 'correct')
    search_fields = ('question',)
    list_filter = ('fan',)
    change_list_template = "admin/test_change_list.html"  # Custom template

    def get_urls(self):
       urls = super().get_urls()
       custom_urls = [
           path('import-excel/', self.import_excel, name="test_import_excel"),
       ]
       return custom_urls + urls
    
    def import_excel(self, request):
        if request.method == "POST":
            form = ExcelImportForm(request.POST, request.FILES)
            if form.is_valid():
                fan = form.cleaned_data["fan"]
                excel_file = request.FILES["excel_file"]
                df = pd.read_excel(excel_file)

                # 📌 Excel fayl tekshiruvi
                required_columns = ["question", "correct", "wrong1", "wrong2", "wrong3"]
                if not all(col in df.columns for col in required_columns):
                    self.message_user(request, "Excel fayl noto'g'ri formatda!", level=messages.ERROR)
                    return redirect("..")

                # 📌 Excel fayldan testlarni yuklash
                for _, row in df.iterrows():
                    try:
                        Test.objects.create(
                            fan=fan,
                            question=row["question"],
                            correct=row["correct"],
                            wrong1=row["wrong1"],
                            wrong2=row["wrong2"],
                            wrong3=row["wrong3"],
                        )
                    except Exception as e:
                        self.message_user(request, f"Xatolik: {str(e)}", level=messages.ERROR)

                self.message_user(request, "Excel fayl muvaffaqiyatli yuklandi!", level=messages.SUCCESS)
                return redirect("..")
        else:
            form = ExcelImportForm()
        
        return render(request, "admin/excel_import.html", {"form": form})


    def get_subjects(self, obj):
        return ", ".join([fan.name for fan in obj.fan.all()])
    
    get_subjects.short_description = "Fanlar"  # Admin panel ustuni nomi



