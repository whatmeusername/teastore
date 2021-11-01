from django.urls import path
from . import views

app_name = 'Catalog'

urlpatterns = [
    path('view/<str:typeslug>/<str:slug>/', views.ViewCatalog, name = 'catalog'),

    path('filter/', views.FilterCatalog, name = 'filter')
]
