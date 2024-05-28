 
 
from django.urls import path
from . import views

#localhost : 8000/firstapp 
#localhost : 8000/firstapp/order

urlpatterns = [
    path('', views.firstapp,name='all_app'),
    # path('order/', views.order,name='order'),
     
]
