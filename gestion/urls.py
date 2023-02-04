from django.urls import path
from .views import CategoriasApiView, PlatosApiView, PlatoDestroyApiView, ListarCategoriaApiView

urlpatterns =[
    path('categorias/',CategoriasApiView.as_view()),
    path('platos/',PlatosApiView.as_view()),
    path('plato/<int:pk>',PlatoDestroyApiView.as_view()),
    path('categoria/<int:pk>',ListarCategoriaApiView.as_view())
]