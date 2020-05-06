from django.urls import path
from .views import index, list, create, view_list

urlpatterns = [
    path('', index, name = 'index_url'),
    path('<int:pk>/', list, name = 'list_url'),
    path('create/', create, name = 'create_url'),
    path('view/', view_list, name = 'view_list_url'),
]
# /Test commit1