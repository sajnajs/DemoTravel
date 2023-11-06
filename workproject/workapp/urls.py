from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('contact/',views.fun1,name='fun1')
]









    # path('add/',views.subtract,name='subtract'),
    # path('add/',views.multiply,name='multiply'),
    # path('add/',views.division,name='division')
    # # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks')
