from django.urls import path


from student import views


urlpatterns = [

 path('', views.index, name='home'),
 
    # path('about/', views.about, name='about'),  # localhost:8000/about/
    # path('team/', views.team, name='team'),  # localhost:8000/team/
    # path('contact/', views.contact, name='contact'),  # localhost:8000/contact/
    # path('services/', views.services, name='services'),  # localhost:8000/services/
]
