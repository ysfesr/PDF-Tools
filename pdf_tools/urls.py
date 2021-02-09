from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf_info', views.info, name='info'),
    path('merge',views.merge, name='merge')
    ]