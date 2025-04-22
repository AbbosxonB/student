from django.db import models

# Create your models here.

class Yunalish(models.Model):  # yo'nalishlar
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt

    def __str__(self):
       return self.name  # Admin panelda sarlavha ko'rsatiladi
    
class Kursi(models.Model):   # 1, 2, 3, 4, 5
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt

    def __str__(self):
       return self.name  # Admin panelda sarlavha ko'rsatiladi
    
class Shakli(models.Model):  # kunduzgi, sirtqi
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt

    def __str__(self):
       return self.name  # Admin panelda sarlavha ko'rsatiladi
    
class Turi(models.Model):  #bakalavr, magistr
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt

    def __str__(self):
       return self.name  # Admin panelda sarlavha ko'rsatiladi
    
class Fan(models.Model):   # fan nomi
    name = models.CharField(max_length=100)
    kursi = models.ManyToManyField(Kursi)
    yunalish = models.ManyToManyField(Yunalish)
    shakli = models.ManyToManyField(Shakli)
    turi = models.ManyToManyField(Turi)   
    smestr= models.IntegerField()
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)   # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)       # Yangilangan vaqt

    def __str__(self):
       return self.name  # Admin panelda sarlavha ko'rsatiladi
    
class Test(models.Model):
    fan = models.ManyToManyField(Fan)
    question = models.TextField(max_length=200)
    correct = models.CharField(max_length=200)
    wrong1 = models.CharField(max_length=200)
    wrong2 = models.CharField(max_length=200)
    wrong3 = models.CharField(max_length=200)
        
    def __str__(self):
        return self.question
    

class Guruh(models.Model):
    name = models.CharField(max_length=100)
    yunalish = models.ManyToManyField(Yunalish)
    kursi = models.ManyToManyField(Kursi)
    shakli = models.ManyToManyField(Shakli)
    turi = models.ManyToManyField(Turi)
    fan = models.ManyToManyField(Fan)
    status = models.CharField(max_length=45, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    



class Natija(models.Model):
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    kurs = models.IntegerField()
    guruh = models.CharField(max_length=50)
    yonalish = models.CharField(max_length=100)
    togri_soni = models.IntegerField()
    umumiy_savollar = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)