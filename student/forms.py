from django import forms
from .models import Team

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team  # Model nomini shu yerga yozing
        fields = [
            "firstname", "lastname", "surename", "malumoti", "manzil", "jinsi",
            "email", "Website", "Github", "telegram", "instagram", "twitter", "facebook",
            "avator", "img", "telefon",
            "Webdesign", "html", "css", "js", "bootstrap", "react",
            "python", "php", "csharp", "goo", "sql"
        ]

        widgets = {
            "firstname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ism"}),
            "lastname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Familiya"}),
            "surename": forms.TextInput(attrs={"class": "form-control", "placeholder": "Otasining ismi"}),
            "malumoti": forms.Select(attrs={"class": "form-select"}),
            "manzil": forms.TextInput(attrs={"class": "form-control", "placeholder": "Manzil"}),
            "jinsi": forms.Select(attrs={"class": "form-select"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "Website": forms.URLInput(attrs={"class": "form-control", "placeholder": "Website"}),
            "Github": forms.TextInput(attrs={"class": "form-control", "placeholder": "Github"}),
            "telegram": forms.TextInput(attrs={"class": "form-control", "placeholder": "Telegram"}),
            "instagram": forms.TextInput(attrs={"class": "form-control", "placeholder": "Instagram"}),
            "twitter": forms.TextInput(attrs={"class": "form-control", "placeholder": "Twitter"}),
            "facebook": forms.TextInput(attrs={"class": "form-control", "placeholder": "Facebook"}),
            "avator": forms.FileInput(attrs={"class": "form-control"}),
            "img": forms.FileInput(attrs={"class": "form-control"}),
            "telefon": forms.TextInput(attrs={"class": "form-control", "placeholder": "Telefon"}),

            # Texnologiyalar uchun progress bar formatida input
            "Webdesign": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "html": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "css": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "js": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "bootstrap": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "react": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "python": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "php": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "csharp": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "goo": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
            "sql": forms.NumberInput(attrs={"class": "form-range", "min": 0, "max": 100}),
        }