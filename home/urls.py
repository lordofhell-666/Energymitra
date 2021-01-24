
from django.urls import path

from home import views


app_name = 'home'

handler404 = 'home.views.handle404'



urlpatterns = [
    path('', views.index , name='index'),
    path('about/', views.about , name='about'),
    path('services/', views.services , name='services'),
    path('projects/', views.projects , name='projects'),
    path('shop/', views.shop , name='shop'),
    path('contact/', views.contact , name='contact'),
    path('sendmail/', views.sendmail , name='sendmail'),
    path('success/', views.successView , name='success'),
    # path('warranty_form/', views.warranty_form , name='warranty_form'),
    path('test/', views.test , name='test'),
    

    path('projects/<slug:project_slug>', views.projectdetail, name='project_detail'),
    path('shop/<slug:product_slug>', views.productdetail, name='product_detail'),

    
]