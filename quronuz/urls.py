from django.urls import path, include
from . import views
urlpatterns = [
    path('' , views.base , name='base'),
    path('qories/' , views.qories, name='qories'),
    path('qori/<slug:slug>/', views.qori, name='qori'),
    path('sura/<slug:slug>/', views.sura, name='sura'),
    path('domlalar/' , views.domlalar, name='domlalar'),
    path('maruzalar/<slug:slug>/' , views.domla, name='domla'),
    path('maruza/<slug:slug>/' , views.maruza, name='maruza'),
]