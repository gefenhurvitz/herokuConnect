from django.contrib import admin
from django.urls import path,include
from . import views as api

urlpatterns = [
    path('test/',api.index ),
    path('products', api.products),
    path('products/<id>', api.products),
    path('up',api.my_view, name='my-view')

]
