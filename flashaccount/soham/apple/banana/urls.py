from django.contrib import admin
from django.urls import path, include
from banana import views

urlpatterns = [
    path("banana/",views.index, name='banana'),
    path('valuetog/', views.valuetog, name='valuetog'),
    path('custcount/', views.cust_count, name='cust_count'),
    path('regcustcount/', views.button_click_view, name='button_click_view')
]