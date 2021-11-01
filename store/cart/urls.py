from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('add/<int:object_id>/', views.AddCart, name='cart_add'),
    #path('remove/', views.RemovefromCart, name='cart_remove'),
    #path('clear/', views.ClearCart, name='cart_clear'),
    #path('delete/', views.DeleteCart, name='cart_delete'),
]