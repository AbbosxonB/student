from django.urls import path


from student import views


urlpatterns = [

 path('', views.form, name='form'),
 path('ajax/kurslar/', views.get_kurslar, name='ajax_kurslar'),
 path('ajax/guruhlar/', views.get_guruhlar, name='ajax_guruhlar'),
 path('ajax/fanlar/', views.get_fanlar, name='ajax_fanlar'),
 path('test/<int:id>/', views.test_views, name='test'),
 # path('tests/', views.test_views, name='tests'),

#  path('form/', views.form, name='form'),
 
    # path('about/', views.about, name='about'),  # localhost:8000/about/
    # path('team/', views.team, name='team'),  # localhost:8000/team/
    # path('contact/', views.contact, name='contact'),  # localhost:8000/contact/
    # path('services/', views.services, name='services'),  # localhost:8000/services/
]
