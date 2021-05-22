from django.urls import path, include

from . import views

app_name = 'myapp2'
urlpatterns = [
    path('', views.homepage, name ='homepage')
]
