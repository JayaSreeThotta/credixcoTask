"""fashionable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fashionableapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.title),
    path('images',views.images),
    path('saree1',views.saree1),
    path('saree2',views.saree2),
    path('saree3',views.saree3),
    path('saree4',views.saree4),
    path('saree5',views.saree5),
    path('saree6',views.saree6),
    path('saree7',views.saree7),
    path('saree8',views.saree8),
    path('saree9',views.saree9),
    path('saree10',views.saree10),
    path('saree11',views.saree11),
    path('saree12',views.saree12),
    path('productsaree1',views.productsaree1),
    path('productsaree2',views.productsaree2),
    path('productsaree3',views.productsaree3),
    path('productsaree4',views.productsaree4),
    path('productsaree5',views.productsaree5),
    path('productsaree6',views.productsaree6),
    path('productsaree7',views.productsaree7),
    path('productsaree8',views.productsaree8),
    path('productsaree9',views.productsaree9),
    path('productsaree10',views.productsaree10),
    path('productsaree11',views.productsaree11),
    path('productsaree12',views.productsaree12)
]
