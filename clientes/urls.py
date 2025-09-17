from django.urls import path
from . import views

app_name = 'clientes'  # <- clave para namespacing

urlpatterns = [
    path('', views.ClienteList.as_view(), name='list'),
    path('nuevo/', views.ClienteCreate.as_view(), name='create'),
    path('<int:pk>/editar/', views.ClienteUpdate.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ClienteDelete.as_view(), name='delete'),
]
