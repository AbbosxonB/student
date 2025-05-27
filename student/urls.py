from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from student import views
from student.views import upload_test

urlpatterns = [

 path('', views.form, name='form'),
 path('ajax/kurslar/', views.get_kurslar, name='ajax_kurslar'),
 path('ajax/guruhlar/', views.get_guruhlar, name='ajax_guruhlar'),
 path('ajax/fanlar/', views.get_fanlar, name='ajax_fanlar'),
 path('start-test/<int:id>/', views.test_views, name='start_test'),
 path('submit-test/<int:fan_id>/', views.submit_test, name='submit_test'),
 path('upload-test/', upload_test, name='upload_test'),

 path('admin/', admin.site.urls),

    # Login
 path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout
 path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

path('dashboard/', views.dashboard, name='dashboard'),


 # path('tests/', views.test_views, name='tests'),

#  path('form/', views.form, name='form'),
 
    # path('about/', views.about, name='about'),  # localhost:8000/about/
    # path('team/', views.team, name='team'),  # localhost:8000/team/
    # path('contact/', views.contact, name='contact'),  # localhost:8000/contact/
    # path('services/', views.services, name='services'),  # localhost:8000/services/
]
