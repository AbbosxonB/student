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



@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct')
    search_fields = ('question',)
    list_filter = ('fan',)
